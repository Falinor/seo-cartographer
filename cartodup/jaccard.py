#! /usr/bin/env python3

import re


def get_shingles(f, size):
    buf = f.read()  # Read the whole file
    regexp = r'[!@#$%^&*()_+-=,<`~.>/?\[{\]};:\'"\\|§±]'
    buf = re.sub(regexp, '', buf)  # Remove special chars
    buf = buf.split()  # Split words using white spaces
    for i in range(0, len(buf) - size + 1):
        yield tuple(buf[i: i + size])  # Yield shingles


def jaccard(file1, file2, shingles_size=3):
    set1 = set(get_shingles(file1, shingles_size))
    set2 = set(get_shingles(file2, shingles_size))
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)
