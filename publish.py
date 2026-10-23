import os
import subprocess
from pathlib import Path

here = Path(__file__).parent
books_file = here / Path("books.txt")
book_files = [b + '.pdf' for b in books_file.read_text().strip().splitlines()]
books_dir = Path(os.environ["BOOKS_DIR"]).expanduser()
server_dir = os.environ["SERVER_DIR"]

# Sync index page
cmd = ['rsync', 'index.html', server_dir]
subprocess.run(cmd, check=True, cwd=here)

# Sync books
cmd = [
    'rsync',
    '--verbose',
    '--archive', # preserve file data and system attributes
    '--partial', '--progress', # show progress for each file
    *book_files,
    server_dir,
]
subprocess.run(cmd, check=True, cwd=books_dir)
