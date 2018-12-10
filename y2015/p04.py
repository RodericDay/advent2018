import hashlib
import itertools


def f(text, n, goal):
    bytes_ = f"{text}{n}".encode()
    return hashlib.md5(bytes_).hexdigest().startswith(goal)


def main(text, simple):
    if simple:
        print(next(n for n in itertools.count() if f(text, n, '00000')))
    else:
        print(next(n for n in itertools.count() if f(text, n, '000000')))
