#!/usr/bin/env python3

import sys

__doc__ = """
Usage: {} [--dict=<filename>] <number>...

<number>...                Numbers to turn into words
                           If -, take <number>... from STDIN.

Options:
  -d, --dict=<filename>    Dictionary file to use
                           [DEFAULT: /usr/share/dict/words]
""".format(sys.argv[0])

from docopt import docopt

def phrases(dictfile, numbers):
  print(dictfile, numbers)
  return []


def main(args):
  print(args)
  with open(args['--dict'], 'r') as dictfile:
    results = phrases(dictfile, [int(x) for x in args['<number>']])


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args)
