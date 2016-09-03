from docopt import docopt


def configure():
    help = """Duplication seo-cartographer

    Usage:
      $ seo-cartographer [options...]

    Options:
      -h, --help            Display this help and exit.
      -f, --file=<path>     Parse the given file, containing URIs to treat.
    """

    args = docopt(help)
    print(args)

if __name__ == '__main__':
    configure()
