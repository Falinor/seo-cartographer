def compare(path: str):
    """Compares given page content with other registered pages,
    and populates a duplication matrix.

    :param path: The path to a file containing what should be compared.
    """
    pass


class Comparator:
    def __init__(self):
        self.matrix = {}

    def add_result(self, url1: str, url2: str, result: float):
        try:
            self.matrix[url2][url1] = result
        except KeyError:
            if self.matrix.get(url1):
                self.matrix[url1][url2] = result
            else:
                self.matrix[url1] = {url2: result}

    def exists(self, url1: str, url2: str):
        try:
            return self.matrix[url1][url2] is not None
        except KeyError:
            return False
