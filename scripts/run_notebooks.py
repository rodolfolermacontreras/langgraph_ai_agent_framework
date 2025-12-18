"""run_notebooks.py

Utility to execute a list of notebooks headlessly using nbclient.

Purpose:
- Used during development to validate playground notebooks run end-to-end in a controlled environment.

Usage:
- Activate the local virtual environment (`.venv`) and run:
  python scripts/run_notebooks.py

Notes:
- This is scaffolding for verification. If this script becomes part of a test harness or CI job, move
  it into an appropriate test runner and add configuration for CI. Otherwise, consider removing it once
  CI-based validation is in place. Any changes to this script should be recorded in `docs/session_memory.md`.
"""

from nbformat import read, write
from nbclient import NotebookClient
from pathlib import Path
import asyncio
import sys

# On Windows the ProactorEventLoop used by default can raise warnings with zmq.
# Use the SelectorEventLoop policy when available to avoid those runtime warnings.
try:
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except Exception:
    pass

NOTEBOOKS = [
    Path('playground/01_basics_overview.ipynb'),
    Path('playground/02_code_examples.ipynb')
]


def execute_notebooks(notebooks, timeout=600):
    """Execute a list of notebooks and write executed copies next to originals.

    Args:
        notebooks (list[Path]): paths to notebooks.
        timeout (int): execution timeout in seconds for each notebook.
    """
    for p in notebooks:
        print('\nExecuting', p)
        nb_doc = read(str(p), as_version=4)
        client = NotebookClient(nb_doc, timeout=timeout, kernel_name='python3')
        try:
            client.execute()
            out_path = p.parent / (p.stem + '.executed.ipynb')
            write(nb_doc, str(out_path))
            print('Wrote executed notebook to', out_path)
        except Exception:
            print('Error executing', p)
            import traceback

            traceback.print_exc()


if __name__ == '__main__':
    execute_notebooks(NOTEBOOKS)
