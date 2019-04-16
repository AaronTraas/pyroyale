from argparse import ArgumentParser, RawDescriptionHelpFormatter
import logging
import os
import sys

from ._version import __version__

logger = logging.getLogger(__name__)

def parse_args(argv):
    # parse command line arguments
    parser = ArgumentParser(prog        = 'pyroyale',
                            description = '''A tool for creating a dashboard for clan participation in
                                             ClashRoyale. See https://developer.clashroyale.com to sign up
                                             for a developer account and create an API key to use with this.''')
    parser.add_argument('--api_key',
                        metavar  = 'KEY',
                        help     = 'API key for developer.clashroyale.com')
    parser.add_argument('--clan',
                        metavar  = 'TAG',
                        help    = 'Clan ID from Clash Royale. If it starts with a "#", clan ID must be quoted.')
    parser.add_argument('--version',
                        action   = 'store_true',
                        help     = 'List the version of crtools.')

    return parser.parse_args(argv)


def main(): # pragma: no cover
    args = parse_args(sys.argv[1:])
