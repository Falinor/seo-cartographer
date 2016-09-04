import cartodup.parser as parser


def test_parse():
    for page in parser.parse('resources/pages.txt'):
        assert page is not None
