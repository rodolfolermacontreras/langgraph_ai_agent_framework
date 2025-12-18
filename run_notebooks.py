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

notebooks = [
    Path('playground/01_basics_overview.ipynb'),
    Path('playground/02_code_examples.ipynb')
]

for p in notebooks:
    print('\nExecuting', p)
    nb_doc = read(str(p), as_version=4)
    client = NotebookClient(nb_doc, timeout=600, kernel_name='python3')
    try:
        client.execute()
        out_path = p.parent / (p.stem + '.executed.ipynb')
        write(nb_doc, str(out_path))
        print('Wrote executed notebook to', out_path)
    except Exception as e:
        print('Error executing', p)
        import traceback

        traceback.print_exc()
