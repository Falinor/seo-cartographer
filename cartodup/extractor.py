import requests
import sys


def extract(url: str) -> list:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            path = 'resources/' + url + '.html'
            with open(path, 'wb') as f:
                f.write(r.text.encode('UTF-8'))
                # TODO: possibly detect write error
            return path
    except requests.ConnectionError as ex:
        msg = 'cartographer: {0} unreachable; this could be caused by a ' \
              'loss of connection\n'.format(url)
        print(msg, file=sys.stderr)


if __name__ == '__main__':
    pass
