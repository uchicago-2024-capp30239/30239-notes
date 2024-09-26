# 30239 Notes Repository

## How to use this Repo

I will push notes to this repository throughout the quarter, so if you are keeping your own notes in this repository you should generally keep them in separate files to avoid accidental git conflicts.

Either make companion files in each directory, or keep your notes in a separate directory/notebook altogether.

## Table of Contents

I will create a directory for each topic, numbered in the order they're introduced.

Inside each directory, you're likely to find:

- `slides.md` - My slides in raw markdown.
- `slides.html` - My slides converted to a presentation. (using [`marp`](https://marpit.marp.app)) You can open this in your web browser (Type `open slides.html` from the command line.)
- `*.ipynb` - These are Jupyter notebooks (see below).

Not every week will have both slides & a notebook.

Other files, such as images & data will be kept in the appropriate folder.

### Jupyter Notebooks

You have a few options for working with `.ipynb` notebooks:

- `uv run jupyter lab` - the newer UI, will start a server and 
- `uv run jupyter notebook` - the older UI, perfectly functional still
- VS Code will open these in it's own editor

If you run one of the `uv run` options, you'll need to navigate to the .ipynb file in the window that opens in your browser.

**Note:** To stop a server, press `Ctrl-C` and then 'y' to the prompt.
