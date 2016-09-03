from docopt import docopt
from extractor import extractor


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
    pages
    import cartodup.comparator.comparator
    extractor.extract(pages)
    # extractor(args['--file'])


if __name__ == '__main__':
    configure()
