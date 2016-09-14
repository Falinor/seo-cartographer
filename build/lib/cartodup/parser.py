def parse(path: str) -> str:
    """Extracts URLs from given file's path.

    :param path: A path to the file containing different URLs to fetch.
    :return: A generator containing lines read from the file.
    :rtype: str
    """
    with open(path) as f:
        for line in f:
            yield line
