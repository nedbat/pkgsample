# COMMANDS. An example of a function to run as a command-line command.
# If you aren't providing a command, you don't need this file.

import sys

import rich

def add_main():
    """Add together the numbers on the command line."""
    nums = [int(a) for a in sys.argv[1:]]
    rich.print(f"Your numbers are: [bold]{nums}[/bold]")

    total = sum(nums)
    rich.print(f"They add up to: [bold]{total}[/bold]")
