# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
from . import __version__


parser = ap.ArgumentParser(prog="optimmizer", formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.set_defaults(__cmd__=parser.print_help)
parser.add_argument('-v', '--version', action='version', version=__version__)


def main():
    args = vars(parser.parse_args())
    cmd = args.pop('__cmd__')
    return cmd(**args)


if __name__ == '__main__':
    main()
