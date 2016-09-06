import re
import requests
import sys


def extract(url: str) -> str:
    try:
        url = url.strip('\n')
        r = requests.get(url)
        if r.status_code == 200:
            url = re.sub(r'http(s)?://', '', url)
            path = 'resources/' + url + '.html'
            with open(path, 'wb') as f:
                f.write(r.text.encode('UTF-8'))
                # TODO: possibly detect write error
            return path
    except requests.ConnectionError as ex:
        msg = 'cartographer: {} unreachable; this could be caused by a ' \
              'loss of connection\n'.format(url)
        print(msg, file=sys.stderr)


if __name__ == '__main__':
    pass
