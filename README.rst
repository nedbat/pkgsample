**Note** Since writing this example, I've discovered that the `Python Packaging
User Guide tutorial`__ is good and serves the same purpose, so you should
use it.

__ https://packaging.python.org/en/latest/tutorials/packaging-projects/

I learned things writing this example, so it wasn't wasted effort.  It's here
if you find it helpful.  Carry on.

-----

#########
pkgsample
#########

.. This file is the documentation for how to use this pkgsample repo.
.. You will replace it with your own file.

This is an example demonstrating how to package your code for distribution on
PyPI.  It is **one possible way** to do it in the fall of 2022.  I am not going
to discuss other ways it could be done. The packaging ecosystem is complex.
Talking about all the options just confuses things.  If you want to know more
about how this page came to be, read the blog post: `One way to package Python
code right now`__.

__ https://nedbatchelder.com/blog/202402/one_way_to_package_python_code_right_now.html

This repo isn't meant to show all of the configuration in a typical project.
For example, it has no tests, it has no docs, it doesn't use linters or type
checkers.  Those are good things, you should look into them, but this repo is
only about packaging a project for distribution, and leaves out those other
good things so we can focus on the packaging.

The files in this repo have comments throughout, to help you understand what
does what, so that you can create your own files with the parts and the details
that you need. Aside from your own source files, there's really only one file
to worry about.


How to use this repo
====================

This repo is a model of how you can configure your project to create
installable packages.  You don't have to copy this whole repo.  You can copy
individual files, because there are only a few you need.  Make a copy of a
file, take the parts that you need, leave out the parts you don't, and edit the
details to match your project.


Decisions
---------

You need to make a few decisions before getting started.

Project name
............

You have to pick a name for your project.  In this repo, it's "pkgsample", but
you will choose a different name.  Your project name will serve a few different
functions: it will be the module name for importing, the name of the repo, and
also the name on PyPI. Anywhere you see "pkgsample," you will change it to your
project name.

Since the project name will be the name on PyPI, you should check to see if
your desired name is available there before making a decision.  `Search for
your name on PyPI <pypi_>`_ to see if it's already taken.

Version number
..............

The version number of your package is in src/pkgsample/__init__.py as the
``__version__`` variable.  You will update this value when making a
distribution.  See the note in "Upload a test" below about using .devN suffixes
initially.

Optional features
.................

This layout will install your modules so that people can import them.  There
is also an extra possibility included:

- You might have commands you need to install so that your users have new
  command-line tools. These parts are marked with ``COMMANDS:``.

Keep an eye out as you look through the files to understand what you can omit
if you don't need this option.

Project details
...............

There are other details that you might want to change, but you don't have to:

- License: this repo uses the Apache license, but you can choose a different
  one.

- Minimum Python version: this repo requires Python 3.9 or greater. Perhaps you
  need to support more versions (choose a lower requirement) or you want to use
  some newer Python features (choose a higher requirement).

Comments throughout the files, especially in pyproject.toml show where to make
these choices, and link to resources that can help.


What's in the repo
==================

This repo is a demonstration of making a distributable package.  You should
examine the files here, decide which are right for you, and adapt them to your
needs.

src/
----

This directory is where you put your code. It should have one subdirectory
named for your project, and all of your work goes into that subdirectory.

This repo has a few small files in src/pkgsample just to have something to
build and distribute. You will delete that directory and make a new
subdirectory for your files.

pyproject.toml
--------------

This is the heart of the process. You will be making lots of changes in this
file.  The metadata about your project (name, description, author, and so on)
are all specified here as well as many other details.

README.rst
----------

(This file!) You will replace this file with your own README.rst describing
your project, how to install it, how to use it, how to get help, the
`changelog`_, and so on.

If you prefer Markdown, make a README.md instead, and change the ``readme``
line in pyproject.toml.

Bits and bobs
-------------

**.gitignore** is a standard git file that keeps uninteresting files from being
stored in git.

**LICENSE.txt** is the text of your chosen license.

Some files here are not needed to get a project distributed, but are useful for
me in this repo, and you might find useful also:

- **Makefile**: organizes the commands needed to work in the repo.  The
  commands shown in this README are also available as targets in the Makefile.
  You can use ``make help`` to see the targets and what they do.

- **.editorconfig**: specifies simple formatting rules that your editor can
  enforce.


Preparing your environment
==========================

Get yourself a Python 3.9 environment.  Using a `virtualenv`_ is recommended
but not required.

You'll need a few tools to build the installable files (called distributions).
They are specified in the dev-requirements.txt file. Install them with pip::

    python -m pip install -r dev-requirements.txt
    # or:  make tools


Make your changes
=================

If you are ready, you can make all your project changes.  If you want, you can
also skip this step to try some of the next steps with the pkgsample repo as it
is, to see what happens.

Copy the files from this repo, then make all your changes:

- Put your project's source files in the src/ directory.  Make sure to remove
  all traces of the pkgsample code.

- Update the pyproject.toml file with all your chosen details.  The word
  "pkgsample" shouldn't appear in it at all when you are done.

- Completely re-write the README.rst file with the description and details of
  your project.


Install locally
===============

You can do some preliminary testing of your project by installing it as an
"editable install" in your current environment::

    python -m pip install -e .

This will make your project importable in your current Python, and you can try
running your code.  Here's an example using the pkgsample code::

    % python
    Python 3.9.15 (main, Oct 24 2022, 17:23:01)
    >>> from pkgsample.add import add
    >>> add(17, 42)
    59

If you are creating command-line commands, you will be able to run them now::

    % pkgsample_add 1 2 3 4 5
    Your numbers are: [1, 2, 3, 4, 5]
    They add up to: 15

By the way, an editable install like this is also a good way to do development,
because Python will import directly from the files you are editing in your
working tree, so it's quick to make changes and see their effect.

Once you do this, you will start seeing ``__pycache__`` directories near your
code.  These contain compiled bytecode files, named something.something.pyc.
You can safely delete these files, and the .gitignore file will keep them from
being stored in git.


Making distributions
====================

You're ready to make installable artifacts, called distributions.

Create the files
----------------

These commands will make the files and check them for correctness::

    python -m build --sdist --wheel
	python -m twine check dist/*
    # or:  make clean dist

If all went well, you will now have a dist/ directory with two files::

    pkgsample-0.1.0-py3-none-any.whl
    pkgsample-0.1.0.tar.gz

The .whl file is a "wheel".  This is the preferred file format for
distributions.  The .tar.gz file is a "source distribution" (sdist), which is
also easy to provide, and is preferred by some users.

If something went wrong, the ``twine check`` command reported errors to fix.
It might help to see what is in the files, or you are just curious.  You can
examine the contents::

    % tar tvfz dist/*.tar.gz
    drwxr-xr-x  0 user group       0 Nov 15 06:25 pkgsample-0.1.0/
    -rw-r--r--  0 user group   10177 Nov 15 05:07 pkgsample-0.1.0/LICENSE.txt
    -rw-r--r--  0 user group   19222 Nov 15 06:25 pkgsample-0.1.0/PKG-INFO
    -rw-r--r--  0 user group    6866 Nov 15 06:24 pkgsample-0.1.0/README.rst
    -rw-r--r--  0 user group    2860 Nov 15 05:28 pkgsample-0.1.0/pyproject.toml
    -rw-r--r--  0 user group      38 Nov 15 06:25 pkgsample-0.1.0/setup.cfg
    drwxr-xr-x  0 user group       0 Nov 15 06:25 pkgsample-0.1.0/src/
    drwxr-xr-x  0 user group       0 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample/
    -rw-r--r--  0 user group     246 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample/__init__.py
    -rw-r--r--  0 user group     166 Nov 15 05:07 pkgsample-0.1.0/src/pkgsample/add.py
    -rw-r--r--  0 user group     410 Nov 15 05:07 pkgsample-0.1.0/src/pkgsample/add_cli.py
    drwxr-xr-x  0 user group       0 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/
    -rw-r--r--  0 user group   19222 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/PKG-INFO
    -rw-r--r--  0 user group     333 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/SOURCES.txt
    -rw-r--r--  0 user group       1 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/dependency_links.txt
    -rw-r--r--  0 user group     113 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/entry_points.txt
    -rw-r--r--  0 user group       5 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/requires.txt
    -rw-r--r--  0 user group      10 Nov 15 06:25 pkgsample-0.1.0/src/pkgsample.egg-info/top_level.txt

The distribution includes all of your files, and also new supporting files made
as part of the packaging process.


Testing the distributions
-------------------------

You can test installing the distribution files.  Make a new virtualenv, and
install directly from one of the files::

    python -m pip install /path/to/pkgsample-0.1.0-py3-none-any.whl

Now you should be able to import and run your modules.

Cleaning up
-----------

The dist/ and build/ directories are created as part of this process.  They
won't be stored in git and you can delete them whenever you want to clean up.
The Makefile includes a target to do this for you::

    make clean


Uploading to PyPI
=================

The final step to making a complete installable package is to upload your
distributions to the `Python Package Index, PyPI <pypi_>`_.  This is where pip
finds packages to install.

(If you've been trying these steps with the pkgsample repo unchanged, you won't
be able to do this, because you can't upload new pkgsample distributions.)

There are actually two PyPI instances: the real one at https://pypi.org, and
also a test one at https://test.pypi.org/ for you to try out distributions
before publishing them for real.

Create accounts
---------------

Register two PyPI accounts, at both https://pypi.org/account/register/ and
https://test.pypi.org/account/register/.  PyPI has a number of options to keep
your account secure, but a simple username and password will get you started.

Upload a test
-------------

Upload your distributions to test.pypi.org.  The twine tool does this::

    python -m twine upload --verbose --repository testpypi dist/*
    # or: make clean dist test_pypi

You will be prompted for your username and password, the progress will be
displayed, and finally you'll get a URL to see what your published package page
will look like::

    % python -m twine upload --verbose --repository testpypi dist/*
    Uploading distributions to https://test.pypi.org/legacy/
    INFO     dist/pkgsample-0.1.1.dev0-py3-none-any.whl (10.4 KB)
    INFO     dist/pkgsample-0.1.1.dev0.tar.gz (10.6 KB)
    INFO     Querying keyring for username
    Enter your username: your_username
    INFO     Querying keyring for password
    Enter your password:
    INFO     username: your_username
    INFO     password: <hidden>
    Uploading pkgsample-0.1.1.dev0-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.6/26.6 kB • 00:00 • 13.1 MB/s
    INFO     Response from https://test.pypi.org/legacy/:
             200 OK
    Uploading pkgsample-0.1.1.dev0.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.7/26.7 kB • 00:00 • 27.1 MB/s
    INFO     Response from https://test.pypi.org/legacy/:
             200 OK

    View at:
    https://test.pypi.org/project/pkgsample/0.1.1.dev0/

**Note:** Once you upload a file to PyPI (even the test server), you cannot fix
something and re-upload it.  You must increment the version number somehow in
order to upload an updated file.  While doing your first tests of your
packaging, it's a good idea to use a ``.devN`` suffix while you work on getting
it right: ``__version__ = "0.1.0.dev0"``.

Check over your page.  Make sure everything looks the way you want, including
the metadata in the left-hand sidebar, and the formatting of the README.  If
you need to fix something, increment the ``.devN`` suffix of your version
number, re-make the distributions, and upload them again.

Upload for real
---------------

Once your package looks right on the test PyPI server, you can upload your
package for real!

Fix the version number to get rid of the ``.devN`` suffix, then make new
distributions, and upload them to PyPI::

    rm -fr build/ dist/ src/*.egg-info
    python -m build --sdist --wheel
    python -m twine check dist/*
    python -m twine upload --verbose dist/*
    # or: make clean dist pypi

Your package is available
-------------------------

Now anyone can install your package by using pip::

    pip install pkgsample

You did it!

.. _changelog: https://keepachangelog.com/
.. _pypi: https://pypi.org
.. _virtualenv: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
