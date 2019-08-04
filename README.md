# python-sibling-import <!-- omit in toc -->

- [TL;DR](#tldr)
  - [Snippet](#snippet)
- [Purpose](#purpose)
- [Example Project](#example-project)
- [How It Works](#how-it-works)

## TL;DR

Put this snippet at the top of any Python file that is not the top
level of your project to import to call code from other folders.

### Snippet

<pre>
if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())
</pre>

## Purpose

This project is intended as an example of how to import sibling packages
when developing in Python. It is based on 3.6.8, I believe it should work
on anything above Python 3.3 based on [Notes from Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html).

In no way do I claim this is the "Pythonic" or right way to make this work,
but I was able to make it work consistently for my other development efforts
and thought others may find this example useful.

Python has documentation on how to [handle imports](https://docs.python.org/3/reference/import.html),
but I found the examples were unhelpful during the development of a project.
The examples using absolute paths seem to assume you are testing from the top
level of your project, and not running individual modules which call a module
found in another folder. There are also examples of [Relative Imports](https://docs.python.org/3/reference/import.html#package-relative-imports)
however these seem to be just a way to avoid spelling out the full path of your
modules, and not something you can leverage during development.

## Example Project

Included below is the project layout and examples of where you would insert
the snippet from above. This project also contains files so that you can test
the results of this yourself.

<pre>
python-sibling-import/
    top_level.py
    sound/
        second_level.py
        effects/
            echo.py
        formats/
            wav_write.py
                {snippet}
                {your code}
</pre>

`top_level.py` can call down to lower packages without issue. However,
if you want to run `wav_write.py` with a call to `echo.py`, this requires
additional work to make functional. You can use the [Snippet](#snippet)
from above at the top of your lower level code to run individually, and still
take advantage of what is written in another folder.

## How It Works

This leverages the Python OS function to get the [Current Working Directory](https://docs.python.org/3/library/os.html#os.getcwd).
Once it has your current working directory, it will add it to the [System Path](https://docs.python.org/3/library/sys.html#sys.path),
which is a variable containing all the search locations for packages/modules
to be loaded. When loading other packages in your project, it will treat them
as if you were working from the top level folder.

The [Snippet](#snippet) assumes that you are opening this project in your
development environment from the top level or root of the project,
and may not work otherwise. To modify the code to be opened from a lower level
of the package, such as in `second_level.py` in Sound rather than
PYTHON-SIBLING-IMPORT, the import statements would need to be modified
to remove the inclusion of `Sound.`
