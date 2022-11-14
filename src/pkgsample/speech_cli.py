"""DATAFILES: the main code for the pkgsample_speech command."""

import importlib.resources
import sys

def speech_main():
    """Show speeches.

    With no arguments, list the available speeches.  With one argument, show
    that speech.
    """
    speeches = importlib.resources.files("pkgsample") / "speeches"
    if len(sys.argv) > 1:
        speech = sys.argv[1]
        with importlib.resources.as_file(speeches / f"{speech}.txt") as path:
            with open(path) as f_speech:
                print(f_speech.read())
    else:
        print("Speeches:")
        for fname in speeches.iterdir():
            if fname.suffix == ".txt":
                print(f"  {fname.stem}")
