#########
pkgsample
#########

This is an example demonstrating how to package your code for distribution on
PyPI.  It is **one possible way** to do it in the fall of 2022.  I am not going to discuss
other ways it could be done. The packaging ecosystem is complex.  Talking about
all the options just confuses things.

This repo isn't meant to show all of the configuration in a typical project.
For example, it has no tests, it has no docs, it doesn't use linters or type
checkers.  Those are good things, you should look into them, but this repo is
focused solely on packaging a project for distribution, and leaves out those
other good things so we can focus on the packaging.

The files in this repo have comments throughout, to help you understand what
does what, so that you can create your own files with the parts and the details
that you need.


How to use this repo
====================

You have code you want to distribute.  This repo is a model of how you can
configure your project.  Make a copy of the files here, take the parts that you
need, and leave out the parts you don't.


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
your desired name is available there before making a decision.

Optional features
.................

This layout will install your modules so that people can import them.  There
are also two extra possibilities included. The parts that support these options
are marked with special comments.

- You might have commands you need to install so that people have new
  command-line tools. These parts are marked with ``COMMANDS:``.

- You might have non-Python data files you need to install. These parts are
  marked with ``DATAFILES:``.

Keep an eye as you look through the files to understand what you can omit if
you don't need these options.


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
your project, how to install it, how to use it, how to get help, and so on.

Bits and bobs
-------------

**.gitignore** is a standard git file that keeps uninteresting files from being
stored in git.

**LICENSE.txt** is the text of your chosen license.

Some files here are not needed to get a project distributed, but are useful for
me in this repo, and you might find useful also:

- **Makefile**: organizes the commands needed to work in the repo.

- **.editorconfig**: specifies simple formatting rules that your editor can
  enforce.

Preparing your environment
==========================



Making distributions
====================

Uploading to PyPI
=================

Testing
=======

You can see what is being included with these commands::

    make clean dist
    tar tvfz dist/*.tar.gz
