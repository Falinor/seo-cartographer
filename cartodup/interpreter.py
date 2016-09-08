import datetime
from docopt import docopt
import os
import re
import sys

import cartodup.comparator as comparator
import cartodup.extractor as extractor
import cartodup.parser as parser


def configure():
    help = """Duplication cartodup

    Usage: cartodup -h | -f <path> [-s <number>]

    Options:
      -f, --file=<path>         Parse the given file, containing URIs to treat.
      -h, --help                Display this help and exit.
      -s, --shingles=<number>   Defines the size of shingles. Default is 3.
      -v, --version             Display project version.
    """

    args = docopt(help)
    execute(args)


def execute(args):
    shingles = 3
    if args['--shingles']:  # Change shingles size if -s is passed
        shingles = int(args['--shingles'])
    comp = comparator.Comparator(shingles)

    for url in parser.parse(args['--file']):
        uri = extractor.extract(url)
        comp.add(uri)
    comp.print_csv(sys.stdout)  # Prints results to stdout

    folder = 'output/'
    if not os.path.exists(folder):  # Create output/ folder anyways
        os.mkdir(folder, 0o755)
    path = '{}{}-{}.csv'.format(folder, datetime.datetime.now(), shingles)
    path = re.sub(r'[-:\s]+', '-', path)
    with open(path, 'w') as f:
        comp.print_csv(f)  # Prints results to the generated csv file

    comp.display()


if __name__ == '__main__':
    configure()
