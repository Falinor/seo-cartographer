import random
import re


def get_shingles(f, shingles_size, max_shingles=-1):
    """

    :param f: The file to read.
    :param shingles_size: The size of shingles.
    :param max_shingles: If filled, this option triggers probabilistic method
    with a maximum of max_shingles shingles.
    :return: An iterator of shingles.
    :rtype: Iterator
    """
    buf = f.read()  # Read the whole file
    regexp = r'[!@#$%^&*()_+-=,<`~.>/?\[{\]};:\'"\\|§±]'
    buf = re.sub(regexp, '', buf)  # Remove special chars
    buf = buf.split()  # Split words using white spaces
    if max_shingles == -1:
        for i in range(0, len(buf) - shingles_size + 1):
            yield tuple(buf[i: i + shingles_size])  # Yield shingles
    else:
        # Probabilistic method: take random shingles from each set
        # TODO: enhance probabilistic method
        # e.g. do not treat an already seen shingle
        for i in range(max_shingles):
            rand = random.randint(0, len(buf) - shingles_size + 1)
            yield tuple(buf[rand: rand + shingles_size])


def jaccard(file1, file2, shingles_size=3) -> float:
    """Computes the jaccard distance between to sets.

    :param file1: The first file to compare.
    :param file2: The second file to compare.
    :param shingles_size: The size of shingles.
    :return: The result of comparison.
    :rtype: float
    """
    set1 = set(get_shingles(file1, shingles_size, 200))
    set2 = set(get_shingles(file2, shingles_size, 200))
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)
