"""
banking4converter

Usage:
  banking4converter -h | --help
  banking4converter --version
Options:
  --version                         Show version.
"""

from docopt import docopt
from converter import __version__ as VERSION

def main():
    arguments = docopt(__doc__, version=VERSION)
