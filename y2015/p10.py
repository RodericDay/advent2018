import itertools


def describe(seq):
    return [c for k, vs in itertools.groupby(seq) for c in [len(list(vs)), k]]


def main(text, simple):
    if simple:
        return

    seq = [int(n) for n in text]

    for _ in range(40):
        seq = describe(seq)
    print(len(seq))

    for _ in range(10):
        seq = describe(seq)
    print(len(seq))
