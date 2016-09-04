import requests


def extract(url: str) -> list:
    r = requests.get(url)
    if r.status_code == 200:
        path = 'resources/' + url + '.html'
        with open(path, 'wb') as f:
            f.write(r.text.encode('UTF-8'))
            # TODO: possibly detect write error
        return path


if __name__ == '__main__':
    pass
