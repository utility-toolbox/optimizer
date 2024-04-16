# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
import configlib
from . import __version__, optimize
try:
    import better_exceptions
    better_exceptions.hook()
except ModuleNotFoundError:
    pass


parser = ap.ArgumentParser(prog="optimizer", formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('-c', '--config', default=".optimizer.yaml",
                    help="Path to the config file")


def main():
    args = vars(parser.parse_args())
    configlib.config.merge(configlib.load(fp=args.pop('config')))
    configlib.config.merge(configlib.load_environ(prefix="OPTIMIZER"))
    return optimize(**args)


if __name__ == '__main__':
    main()
