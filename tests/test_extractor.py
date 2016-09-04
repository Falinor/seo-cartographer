import cartodup.extractor as extractor

def test_extract():
    url = 'https://google.fr'
    path = extractor.extract(url)
    assert path is not None

    with open(path) as f:
        assert f.readline() is not None
