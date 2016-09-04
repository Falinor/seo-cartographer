import requests


def extract(url: str) -> list:
    r = requests.get(url)
    if r.status_code == 200:
        with open(url + '.html', 'wb') as f:
            f.write(r.text.encode('UTF-8'))


if __name__ == '__main__':
    pass
