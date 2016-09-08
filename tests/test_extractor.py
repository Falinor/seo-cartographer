import cartodup.extractor as extractor


HTTP_URL = 'http://www.speedtest.net/'
HTTPS_URL = 'https://google.fr/'


def test_strip_protocol():
    url = extractor.URL(HTTP_URL)
    expected = 'www.speedtest.net/'
    actual = url.strip_protocol()

    assert actual == expected


def test_get_resource():
    # HTTP URL
    url = extractor.URL(HTTP_URL)
    expected = 'resources/www-speedtest-net.html'
    actual = url.get_resource()

    assert actual is not None
    assert actual == expected

    # HTTPS URL
    url = extractor.URL(HTTPS_URL)
    expected = 'resources/google-fr.html'
    actual = url.get_resource()

    assert actual is not None
    assert actual == expected
