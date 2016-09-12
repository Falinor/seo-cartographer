import os
import re
import requests
import sys


class URL:
    def __init__(self, url: str):
        """Initializes an URL instance.

        :param url: The URL string to wrap.
        """
        self.url = url
        self.resource = None

    def strip_protocol(self) -> str:
        """See strip_protocol_static."""
        return URL.strip_protocol_static(self.url)

    def get_resource(self) -> str:
        """

        :return:
        """
        if not self.resource:
            self.resource = URL.get_resource_static(self.url)
        return self.resource

    @staticmethod
    def strip_protocol_static(url: str) -> str:
        """Removes the protocol from an URL string e.g. removing http/https/....

        :param url: The URL string to treat.
        :return: The URL string without the protocol.
        :rtype: str
        """
        return re.sub(r'^[a-zA-Z0-9]+?://', '', url, count=1)

    @staticmethod
    def get_resource_static(url: str) -> str:
        """Removes the protocol and replaces all special chars in the given URL
        by a dash, providing a better filename to save on disk.

        :param url: The URL string to treat.
        :return: A path to an HTML resource obtained from the given URL.
        """
        url = URL.strip_protocol_static(url)
        res = re.sub(r'[/.,?]+', '-', url).rstrip('-')
        return 'resources/{}.html'.format(res)


def extract(url: str) -> URL:
    """Fetches an URL string, saves HTML data to a disk file and returns the
    given URL as an URL object.

    :param url: The URL to fetch from.
    :return: The URL object built with the given string.
    """
    try:
        url = url.strip('\n')
        r = requests.get(url)
        url = URL(url)
        if r.status_code == 200:
            path = url.get_resource()
            # Create resources directory anyways
            if not os.path.exists('resources'):
                os.mkdir('resources', 0o755)
            with open(path, 'wb') as f:
                f.write(r.text.encode('UTF-8'))
                # TODO: possibly detect write error
            return url
    except requests.ConnectionError:
        msg = 'cartographer: {} unreachable; this could be caused by a ' \
              'loss of connection\n'.format(url)
        print(msg, file=sys.stderr)


if __name__ == '__main__':
    pass
