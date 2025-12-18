# Session Memory: Iteration Log

This file records the major actions, decisions, and artifacts produced during interactive work sessions. Use this as a living document to capture "why" we changed things, where helper code lives, and which artifacts should be moved into `scripts/` or removed.

## 2025-12-17: Notebook validation and tidy-up

- Purpose: Validate playground notebooks run in `.venv`, fix issues, and document results.

- Actions performed:
  - Made `playground/01_basics_overview.ipynb` robust to `.env` location by implementing `find_upwards()` and `load_dotenv_if_present()`.
  - Made `playground/02_code_examples.ipynb` self-contained (local `Memory` class, improved tool stubs, and agent example).
  - Created `run_notebooks.py` to run notebooks headlessly using `nbclient`. This runner sets the Windows selector event loop policy for more stable headless execution on Windows.
  - Executed both notebooks in `.venv` and saved executed artifacts (`*.executed.ipynb`) for verification.
  - Updated `docs/roadmap.md` with a Mermaid flow diagram and added an Execution Log describing these operations.
  - Updated `README.md` with the current directory tree and a short action plan.

- Files created/modified this session:
  - Modified: `playground/01_basics_overview.ipynb` (loader + memory improvements)
  - Modified: `playground/02_code_examples.ipynb` (self-contained)
  - Added: `run_notebooks.py` (temporary runner)
  - Added: `playground/01_basics_overview.executed.ipynb` (artifact)
  - Added: `playground/02_code_examples.executed.ipynb` (artifact)
  - Modified: `docs/roadmap.md` (diagram + execution log)
  - Modified: `README.md` (directory tree + plan)
  - Added: `docs/session_memory.md` (this file)

- Decisions and rationale:
  - Keep helper code small and in-notebook while it's experimental. If a helper grows or is reused across notebooks, move it into `scripts/` (or a package) and reference it from notebooks.
  - Executed notebook artifacts are helpful for validation, but they should not be permanent members of the repo. Decide whether to keep or remove them (see roadmap/execution log). Prefer ignoring them in `.gitignore` and keeping local copies.

- Next steps (short):
  1. Decide whether to remove `*.executed.ipynb` files from the repo and add them to `.gitignore` (recommended). If yes, I will remove tracking and update `.gitignore`.
  2. Choose the next focused playground notebook to create (RAG recommended). I will draft it and make it self-contained with toggles for enabling Foundry.
  3. When helper functions are stabilized (used across >1 notebook), move them into `scripts/` and document their interface in this file.

- Notes about running code (rules):
  - Always use the local virtual environment (`.venv`) to install packages and run scripts. Do not install packages globally.
  - Keep this `session_memory.md` updated as we change or move helper code.

## Team Rules (improved)

Purpose: a concise, enforceable set of rules to keep the workspace tidy, auditable, and reproducible.

1. Documentation and notes
  - Do not create new top-level documents unless explicitly requested. Prefer updating an existing file under `docs/`.
  - Each doc update must include: what we evaluated, the results, and the explicit reason for changes (if code changed).
  - Add a short "Plan" section at the end of any documentation update summarizing next steps and scope.

2. Scripts and helper code
  - Small helper functions may remain in notebooks while experimental. When a helper is used by more than one notebook or becomes non-trivial, move it into `scripts/` as a module.
  - When creating a script for evaluation, add a short header comment describing purpose, inputs, outputs, and how it will be integrated or removed.
  - Remove or archive experimental scripts after they are integrated into the codebase; record the removal in `session_memory.md`.

3. Environment and packages
  - Always use the local virtual environment (`.venv`) for installs and execution. NEVER install packages globally on developer machines.
  - Record package installs and environment changes in `requirements.txt` or `pyproject.toml` as applicable.

4. Repository hygiene
  - Avoid committing large binary outputs or temporary artifacts. If an executed notebook or artifact is only for local verification, add it to `.gitignore` and remove it from Git history if already committed (coordinate before history rewrite).
  - Keep the repo structure minimal and tidy. If old data or artifacts are no longer needed, remove them and note the deletion in `session_memory.md`.

5. Commits and change management
  - Commit grouped, thematic changes together with clear messages. For significant changes, include a short description of the motivation and rollback plan in the commit message.
  - Push changes to the remote frequently for visibility; use feature branches for large or risky changes.

6. Notes and style
  - Do not use emojis in code, documentation, or commits.
  - Use clear, descriptive names for scripts, variables, and notebooks.

## Session Note Template (use for every update)

Use this template when recording session updates in `docs/session_memory.md`.

- Date: YYYY-MM-DD
- Purpose: Short one-line purpose of the session
- Actions performed: bullet list of main actions (files changed, scripts run)
- Why: short rationale for the actions
- Results: what succeeded, what failed, notable outputs
- Files changed: list of files added/modified/removed
- Next steps / Plan: what to do next (1-3 items)
- Notes: any extra details, security notes, or coordination needed

---

Append future session notes to the top of this file so the most recent work is easy to find.



