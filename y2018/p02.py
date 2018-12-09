import collections
import itertools


def main(text, simple):
    lines = text.splitlines()
    if simple:
        S = lambda line: {v for v in collections.Counter(line).values()}
        a, b = zip(*[(2 in s, 3 in s) for line in lines for s in [S(line)]])
        print(sum(a) * sum(b))
    else:
        for A, B in itertools.combinations(lines, 2):
            same = ''.join(a for a, b in zip(A, B) if a == b)
            if len(A) - len(same) == 1:
                print(same)
                return
