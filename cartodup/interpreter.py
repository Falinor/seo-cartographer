from docopt import docopt

import cartodup.extractor as extractor
import cartodup.parser as parser


def configure():
    help = """Duplication cartodup

    Usage: cartodup -h | -f <path>

    Options:
      -f, --file=<path>     Parse the given file, containing URIs to treat.
      -h, --help            Display this help and exit.
      -v, --version         Display project version.
    """

    args = docopt(help)
    execute(args)


def execute(args):
    url = parser.parse(args['--file'])
    content = extractor.extract(url)
    # extractor(args['--file'])


if __name__ == '__main__':
    configure()
