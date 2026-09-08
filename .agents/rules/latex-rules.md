# LaTeX & Proof Writing Standards for ByteBoost 2026

- **Formal Statements & Proofs**: In bidirectional ("if and only if") proofs, explicitly signpost both directions with `\textbf{($\Longrightarrow$)}` first, then `\textbf{($\Longleftarrow$)}`.
- **Introducing Formal Objects**: Use `Let` (for chosen or assumed objects) or `Define` (for new objects). Never use `Fix`, `Put`, `Set`, `Write`, or `Take`.
- **Display Math & Numbering**: Only assign equation numbers/tags to displays that are explicitly cited via `\eqref` or name in the prose.
- **Tuples & Glosses**: Gloss tuple components strictly in their left-to-right definition order.
- **AI Vocabulary**: Avoid artificial connectives (`whence`, `moreover`, `furthermore`) and buzzwords (`delve`, `leverage`, `tapestry`, `vital`, `crucial`). State steps directly.
- **Quality Gate**: After editing `.tex` files, compile and verify with `bash scripts/check-latex.sh` (must pass with 0 errors, 0 warnings, 0 overfull/underfull boxes). Rebuild committed PDF with `bash scripts/compile.sh`.
