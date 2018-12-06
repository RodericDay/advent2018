import functools
import operator


def round(sequence, alist, i, counter):
    for length in sequence:
        mlist = alist[i:] + alist[:i]
        mlist[:length] = mlist[:length][::-1]
        alist[:] = mlist[-i:] + mlist[:-i]
        i = (i + length + counter) % len(alist)
        counter += 1
    return alist, i, counter


def knot_hash(string):
    sequence = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    alist, i, counter = list(range(256)), 0, 0
    for _ in range(64):
        alist, i, counter = round(sequence, alist, i, counter)

    g = iter(alist)
    dense = [functools.reduce(operator.xor, group) for group in zip(*[g] * 16)]
    hashed = ''.join(f'{n:0>2x}' for n in dense)
    return hashed


def main(text, simple):
    if simple:
        sequence = [int(n) for n in text.split(',')]
        alist, i, counter = list(range(256)), 0, 0
        alist, i, counter = round(sequence, alist, i, counter)
        print(alist[0] * alist[1])

    else:
        print(knot_hash(text))
