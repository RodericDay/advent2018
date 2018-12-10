import re


def advance(ints):
    for i in reversed(range(len(ints))):
        ints[i] += 1
        if ints[i] > ord('z'):
            ints[i] = ord('a')
        else:
            break


def valid(ints):
    g3 = zip(ints, ints[1:], ints[2:])
    yield any(b - a == 1 and c - b == 1 for a, b, c in g3)
    yield not set(ints) & {ord('o'), ord('i'), ord('l')}
    yield len(re.findall(r'(.)(\1)', ''.join(chr(n) for n in ints))) >= 2


def main(text, simple):
    if simple:
        return

    ints = [ord(n) for n in text]
    while not all(valid(ints)):
        advance(ints)

    print(''.join(chr(n) for n in ints))

    advance(ints)
    while not all(valid(ints)):
        advance(ints)

    print(''.join(chr(n) for n in ints))
