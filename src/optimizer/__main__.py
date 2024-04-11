# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
from . import __version__, optimize
try:
    import better_exceptions
    better_exceptions.hook()
except ModuleNotFoundError:
    pass


parser = ap.ArgumentParser(prog="optimizer", formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--version', action='version', version=__version__)


def main():
    args = vars(parser.parse_args())
    return optimize(**args)


if __name__ == '__main__':
    main()
