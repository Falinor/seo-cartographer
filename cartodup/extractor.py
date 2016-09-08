import os
import re
import requests
import sys


class URL:
    def __init__(self, url: str):
        self.url = url
        self.resource = None

    def strip_protocol(self) -> str:
        return URL.strip_protocol_static(self.url)

    def get_resource(self) -> str:
        if not self.resource:
            self.resource = URL.get_resource_static(self.url)
        return self.resource

    @staticmethod
    def strip_protocol_static(url: str) -> str:
        return re.sub(r'^[a-zA-Z0-9]+?://', '', url, count=1)

    @staticmethod
    def get_resource_static(url: str) -> str:
        url = URL.strip_protocol_static(url)
        res = re.sub(r'[/.,?]+', '-', url).rstrip('-')
        return 'resources/{}.html'.format(res)


def extract(url: str) -> URL:
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
    except requests.ConnectionError as ex:
        msg = 'cartographer: {} unreachable; this could be caused by a ' \
              'loss of connection\n'.format(url)
        print(msg, file=sys.stderr)


if __name__ == '__main__':
    pass
