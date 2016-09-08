import cartodup.comparator as comparator
import cartodup.extractor as extractor


HTTP_URL = 'http://www.speedtest.net/'
HTTPS_URL = 'https://google.fr/'


def test_add():
    url1 = extractor.extract(HTTP_URL)
    comp = comparator.Comparator()
    comp.add(url1)
    assert len(comp.matrix) == 1
    assert comp.matrix[url1.url] == {}

    url2 = extractor.extract(HTTPS_URL)
    comp.add(url2)
    assert len(comp.matrix) == 2
    assert comp.matrix[url2.url] == {}
    assert comp.matrix[url1.url][url2.url] >= 0.0
    assert comp.matrix[url1.url][url2.url] <= 1.0


def test_matrix():
    comp = comparator.Comparator()
    assert comp.matrix is not None
    assert comp.matrix == {}

    url = comparator.URL(HTTP_URL)

    comp.matrix[url.url] = 42
    assert comp.matrix[url.url] == 42

    url = comparator.URL(HTTPS_URL)

    comp.matrix[url.url] = 21
    assert comp.matrix[url.url] == 21
