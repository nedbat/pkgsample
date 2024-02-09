# COMMANDS. An example of a function to run as a command-line command.
# If you aren't providing a command, you don't need this file.

import sys

import rich

from .add import add

# This file and function are mentioned in pyproject.toml in the
# [project.scripts] section, like this:
#
#   [project.scripts]
#   pkgsample_add = "pkgsample.add_cli:add_main"
#

def add_main():
    """Add together the numbers on the command line."""
    nums = [int(a) for a in sys.argv[1:]]
    rich.print(f"Your numbers are: [bold]{nums}[/bold]")

    total = 0
    for num in nums:
        total = add(total, num)

    rich.print(f"They add up to: [bold]{total}[/bold]")
