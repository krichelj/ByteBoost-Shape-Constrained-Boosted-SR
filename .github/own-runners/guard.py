"""Own-runners guard: this repo's Actions run on Sanders or Godel, and nowhere else.

Vendored into each repo as .github/own-runners/guard.py by the own-ci-runners
skill, and run by .github/workflows/own-runners-guard.yml on every push and pull
request (any branch), on every other workflow's run (requested and completed),
every six hours, and on demand. Each event proves something different:

  every event      the machine running this step is Sanders or Godel
                   (hostname, RUNNER_ENVIRONMENT, runner name), so the guard
                   itself is never a hosted job that would vouch for the rest
  push, PR,        every job of every workflow in this checkout asks for the
  dispatch         own pool ([self-hosted, linux]), matrix values included, and
                   the guard listens to every workflow by name
  workflow_run     requested: a run with any job asking for a GitHub-hosted
                   machine is cancelled before it spends minutes; completed:
                   every job of the run executed on a sanders-/godel- runner
  schedule         GitHub's record of the last day's runs, GitHub's own
                   Dependabot and Pages runs included, shows no hosted job

Exit 1 names every violation. Needs PyYAML (the workflow runs this under
`uv run --with pyyaml`), the GITHUB_* variables Actions sets, and a token with
actions: write (to cancel).
"""

from __future__ import annotations

import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

#: GitHub's JSON, as the API returns it; a Record is one object (a job, run, runner).
type Json = dict[str, Json] | list[Json] | str | int | float | bool | None
type Record = dict[str, Json]

HOSTS = {"lcs-pashakar-02": "sanders", "lcs-pashakar": "godel"}
OWN_LABELS = frozenset({"self-hosted", "linux", "x64", "sanders", "godel"})
OWN_RUNNER_NAME = re.compile(r"^(sanders|godel)-(site|jit)-[A-Za-z0-9._-]+$")
GUARD_FILES = ("own-runners-guard.yml", "own-runners-guard.yaml")
WORKFLOWS = Path(".github/workflows")
JOBS_APPEAR_SECS = 90

problems: list[str] = []


def check(ok: bool, line: str) -> None:
    print(f"{'ok  ' if ok else 'FAIL'}  {line}")
    if not ok:
        problems.append(line)


# ------------------------------------------------------------- static rules


def labels_are_own(value: Json) -> bool:
    labels = [value] if isinstance(value, str) else value
    if not isinstance(labels, list) or not labels or not all(isinstance(x, str) for x in labels):
        return False
    return "self-hosted" in labels and set(labels) <= OWN_LABELS


def runs_on_violations(job_id: str, job: Record) -> list[str]:
    """Why a job could run somewhere other than the own pool ([] when it cannot)."""
    if "uses" in job:  # a reusable workflow: its own file is checked as a workflow
        return []
    runs_on = job.get("runs-on")
    if isinstance(runs_on, dict):  # runs-on: {group:, labels:}
        runs_on = runs_on.get("labels")
    out = []
    if isinstance(runs_on, str) and "${{" in runs_on:
        m = re.fullmatch(r"\$\{\{\s*matrix\.([A-Za-z0-9_-]+)\s*\}\}", runs_on.strip())
        matrix = ((job.get("strategy") or {}).get("matrix") or {}) if m else {}
        values = (
            list(matrix.get(m.group(1), []))
            if m and isinstance(matrix.get(m.group(1)), list)
            else []
        )
        values += [
            inc[m.group(1)]
            for inc in matrix.get("include", []) or []
            if m and isinstance(inc, dict) and m.group(1) in inc
        ]
        if not values:
            out.append(f"job '{job_id}' runs-on {runs_on!r} cannot be resolved to the own pool")
        out += [
            f"job '{job_id}' matrix runs-on value {v!r} is not the own pool"
            for v in values
            if not labels_are_own(v)
        ]
    elif not labels_are_own(runs_on):
        out.append(f"job '{job_id}' runs-on {runs_on!r} is not the own pool [self-hosted, linux]")
    for key in ("container", "services"):
        if key in job:
            out.append(
                f"job '{job_id}' uses {key}:, which needs docker - unusable on Sanders/Godel for this user"
            )
    return out


def workflow_violations(path: Path, text: str) -> list[str]:
    doc = yaml.safe_load(text)
    if not isinstance(doc, dict) or not isinstance(doc.get("jobs"), dict):
        return []
    out = []
    for job_id, job in doc["jobs"].items():
        out += [
            f"{path}: {v}" for v in runs_on_violations(job_id, job if isinstance(job, dict) else {})
        ]
    return out


def workflow_name(path: Path, doc: Record) -> str:
    """The name GitHub matches workflow_run on: `name:`, else the file's path."""
    return str(doc.get("name") or f".github/workflows/{path.name}")


def guard_listens_to(guard_doc: Record) -> set[str]:
    on = guard_doc.get("on", guard_doc.get(True)) or {}
    return set(((on.get("workflow_run") or {}).get("workflows")) or [])


def static_checks(root: Path) -> None:
    files = sorted(p for p in (root / WORKFLOWS).glob("*") if p.suffix in (".yml", ".yaml"))
    guard = next((p for p in files if p.name in GUARD_FILES), None)
    check(guard is not None, f"{WORKFLOWS} has the own-runners guard workflow")
    listened = guard_listens_to(yaml.safe_load(guard.read_text())) if guard else set()
    for path in files:
        text = path.read_text()
        bad = workflow_violations(path.relative_to(root), text)
        check(
            not bad,
            f"{path.name}: every job asks for the own pool"
            + ("" if not bad else ": " + "; ".join(bad)),
        )
        doc = yaml.safe_load(text)
        if path != guard and isinstance(doc, dict) and isinstance(doc.get("jobs"), dict):
            name = workflow_name(path, doc)
            check(name in listened, f"the guard listens to '{name}' ({path.name}) on workflow_run")


# ------------------------------------------------------------- the machine


def host_checks(env: dict[str, str], hostname: str) -> None:
    short = hostname.split(".")[0].lower()
    host = HOSTS.get(short)
    check(host is not None, f"this step executes on {short} ({host or 'NOT Sanders or Godel'})")
    check(
        env.get("RUNNER_ENVIRONMENT") == "self-hosted",
        f"RUNNER_ENVIRONMENT={env.get('RUNNER_ENVIRONMENT')}",
    )
    name = env.get("RUNNER_NAME", "")
    check(
        bool(host) and name.startswith(f"{host}-") and bool(OWN_RUNNER_NAME.match(name)),
        f"its runner {name or '(unnamed)'} belongs to {short}",
    )


# ------------------------------------------------------------- GitHub's record


def api(method: str, path: str) -> Json:
    req = urllib.request.Request(
        f"{os.environ.get('GITHUB_API_URL', 'https://api.github.com')}/{path}", method=method
    )
    req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req, timeout=30) as res:
        body = res.read()
        return json.loads(body) if body else None


def job_violation(job: Record) -> str | None:
    """Why a job did not run on our machines, or None when it did or never ran."""
    if job.get("conclusion") == "skipped":
        return None
    name = job.get("runner_name") or ""
    if not name:
        # Never started: still waiting, or cancelled before any runner took it.
        waiting = job.get("status") in ("queued", "waiting", "pending")
        return None if waiting or job.get("conclusion") == "cancelled" else "no runner recorded"
    if not OWN_RUNNER_NAME.match(name):
        return f'ran on "{name}"'
    if "self-hosted" not in (job.get("labels") or []):
        return f"labels {job.get('labels')} do not ask for self-hosted"
    return None


def hosted_request(job: Record) -> bool:
    """A job that asks for a machine the own pool cannot be."""
    labels = job.get("labels") or []
    return bool(labels) and not labels_are_own(labels)


def run_checks(repo: str, run: Record, action: str) -> None:
    jobs: list[Record] = []
    deadline = time.time() + (JOBS_APPEAR_SECS if action == "requested" else 0)
    while True:
        jobs = api("GET", f"repos/{repo}/actions/runs/{run['id']}/jobs?per_page=100")["jobs"]
        if jobs or time.time() >= deadline:
            break
        time.sleep(5)
    label = f"run {run['id']} ({run.get('path') or run.get('name')}, {run.get('head_branch')})"
    if action == "requested":
        hosted = [j for j in jobs if hosted_request(j)]
        if hosted:
            try:
                api("POST", f"repos/{repo}/actions/runs/{run['id']}/cancel")
                cancelled = "cancelled it"
            except urllib.error.HTTPError as err:
                cancelled = f"could not cancel it (HTTP {err.code})"
            check(
                False,
                f"{label} asks for GitHub-hosted machines in {[j['name'] for j in hosted]}; {cancelled}",
            )
        else:
            check(True, f"{label}: {len(jobs)} job(s), none asks for a GitHub-hosted machine")
        return
    for job in jobs:
        why = job_violation(job)
        check(
            why is None,
            f"{label} / {job['name']}: {job.get('runner_name') or '-'}"
            + (f" - {why}" if why else ""),
        )
    check(bool(jobs), f"{label}: {len(jobs)} job(s) examined")


def audit(repo: str, hours: int = 24) -> None:
    since = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - hours * 3600))
    runs = api("GET", f"repos/{repo}/actions/runs?created=%3E%3D{since}&per_page=100")[
        "workflow_runs"
    ]
    for run in runs:
        for job in api("GET", f"repos/{repo}/actions/runs/{run['id']}/jobs?per_page=100")["jobs"]:
            why = job_violation(job)
            if why:
                check(False, f"run {run['id']} ({run['path']}) / {job['name']}: {why}")
    check(True, f"audit: {len(runs)} run(s) of the last {hours}h examined")


def main() -> int:
    env = dict(os.environ)
    event = env.get("GITHUB_EVENT_NAME", "")
    host_checks(env, socket.gethostname())
    if event in ("push", "pull_request", "pull_request_target", "workflow_dispatch", ""):
        static_checks(Path("."))
    if event == "workflow_run":
        payload = json.loads(Path(env["GITHUB_EVENT_PATH"]).read_text())
        run_checks(
            env["GITHUB_REPOSITORY"], payload["workflow_run"], payload.get("action", "completed")
        )
    if event in ("schedule", "workflow_dispatch"):
        audit(env["GITHUB_REPOSITORY"])
    print(f"\nown-runners guard: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
