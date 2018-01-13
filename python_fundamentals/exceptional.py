'''A module for demostrating exceptions.'''

import sys
from math import log


def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
            file=sys.stderr)
        raise

def string_log(s):
    x = convert(s)
    return log(x)

# convert(3)
# convert("33")
# convert("hello world")
# convert([1, 4])

string_log("cat")
