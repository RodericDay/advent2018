import re
import collections


def main(text, simple):
    d = collections.Counter()

    for line in text.splitlines():
        i, x, y, w, h = [int(n) for n in re.findall(r'\d+', line)]
        for xi in range(x, x+w):
            for yi in range(y, y+h):
                d[xi, yi] += 1

    if simple:
        print(sum(v > 1 for v in d.values()))

    else:
        for line in text.splitlines():
            i, x, y, w, h = [int(n) for n in re.findall(r'\d+', line)]
            total = {d[xi, yi]
                for xi in range(x, x+w)
                for yi in range(y, y+h)
            }
            if total == {1}:
                print(i)
                return
