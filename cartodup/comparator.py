from cartodup.extractor import URL
import cartodup.jaccard as jaccard


class Comparator:
    def __init__(self, shingles_size=3):
        self.shingles_size = shingles_size
        self.matrix = {}

    def add(self, url: URL):
        """Adds an URL to the matrix after having computed a duplication
        ratio for each other URL.

        :param url:
        :return:
        """
        print('Adding {}'.format(url.url))
        self.__compare_full(url)

    def print_csv(self, out):
        print('Page1;Page2;Shingles_size;Similarity', file=out)
        for key, val in self.matrix.items():
            for v in val:
                print('{};{};{};{}'.format(key,
                                           v,
                                           self.shingles_size,
                                           self.matrix[key][v],
                                           ), file=out)

    def display(self):
        # TODO: display graphics

    def __add_result(self, url1: str, url2: str, result: float):
        """Adds the result of a comparison between two URLs into the
        duplication matrix.

        :param url1:
        :param url2:
        :param result:
        :return:
        """
        try:
            self.matrix[url2][url1] = result
        except KeyError and TypeError:
            if self.matrix.get(url1):
                self.matrix[url1][url2] = result
            else:
                self.matrix[url1] = {url2: result}

    def __compare(self, url1: URL, url2: str) -> float:
        """Compares two URLs page content, giving their duplication
        ratio e.g. the percentage of similar content.

        :param url1:
        :param url2:
        :return:
        """
        path1 = url1.get_resource()
        path2 = URL.get_resource_static(url2)

        with open(path1) as f1, open(path2) as f2:
            return jaccard.jaccard(f1, f2, self.shingles_size)

    def __compare_full(self, url: URL):
        """Compares an URL to each other URL contained in the matrix.

        :param url:
        :return:
        """
        if not self.matrix.get(url.url):
            self.matrix[url.url] = {}

        for key, val in self.matrix.items():
            if url.url == key:
                continue
            print('Comparing: \n\t{} \n\t{}\n'.format(url.url, key))
            res = self.__compare(url, key)
            self.__add_result(url.url, key, res)

    def __exists(self, url1: URL, url2: URL):
        """Checks whether a relationship already exists between two URLs.

        :param url1:
        :param url2:
        :return:
        """
        try:
            return self.matrix[url1.url][url2.url] is not None
        except KeyError:
            return False
