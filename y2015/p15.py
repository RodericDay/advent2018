import functools
import operator
import re


def knap(N, n):
    if n == 1:
        yield [N]
    else:
        for i in range(N + 1):
            for tail in knap(N - i, n - 1):
                yield [i] + tail


def main(text, simple):
    if simple:
        return

    lines = text.splitlines()
    vals = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

    best = 0
    best_lite = 0
    for qty in knap(100, len(lines)):
        weighted = [[q * v for v in vs] for q, vs in zip(qty, vals)]
        subs = [sum(category) for category in zip(*weighted)]
        score = functools.reduce(operator.mul, [max(0, n) for n in subs[:4]])
        if score > best:
            best = score
        if subs[-1] == 500 and score > best_lite:
            best_lite = score

    print(best)
    print(best_lite)
