from docopt import docopt

help = """Duplication cartographer

Usage:
  -h, --help            Display this help and exit.
  -f, --file=<path>     Parse the given file, containing URIs to treat.
"""

args = docopt(help)
print(args)
