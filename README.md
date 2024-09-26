# 30239 Notes Repository

## How to use this Repo

I will push notes to this repository throughout the quarter, so if you are keeping your own notes in this repository you should generally keep them in separate files to avoid accidental git conflicts.

Either make companion files in each directory, or keep your notes in a separate directory/notebook altogether.

## Table of Contents

I will create a directory for each topic, numbered in the order they're introduced.

Inside each directory, you're likely to find:

- `slides.md` - My slides in raw markdown.
- `slides.html` - My slides converted to a presentation. (using [`marp`](https://marpit.marp.app)) You can open this in your web browser (Type `open slides.html` from the command line.)
- `*-notebook.py` - These are marimo notebooks (see below).

Not every week will have slides & a notebook, but one or the other should generally exist.

Other files, such as images & data will be kept in the appropriate folder.

### Marimo Notebooks

Marimo notebooks are similar to Jupyter notebooks, but work much better with Git and have some other nice features I appreciate.

If you have ever looked at a Jupyter notebook file (.ipynb) in an editor, you know they are large JSON files, and once they are checked into Git changes become very difficult to track.

To interact with a notebook, run:

`uv run marimo edit <notebook-file>`

