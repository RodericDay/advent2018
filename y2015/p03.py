import collections
import itertools


def main(text, simple):
    steps = [{'^': -1j, '<': -1, '>': 1, 'v': 1j}[m] for m in text]
    counter = lambda steps: collections.Counter(itertools.accumulate(steps))
    if simple:
        print(len(counter(steps)))
    else:
        print(len(counter(steps[::2]) + counter(steps[1::2])))
