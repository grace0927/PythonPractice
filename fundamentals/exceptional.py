"""A module for demostrating exceptions."""

import os
import sys
from math import log


def convert(s):
    """Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
            file=sys.stderr)
        raise


def string_log(s):
    x = convert(s)
    return log(x)


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, sys.stderr)
        raise
    finally:
        os.chdir(original_path)

# convert(3)
# convert("33")
# convert("hello world")
# convert([1, 4])


string_log("cat")
