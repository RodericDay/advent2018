import itertools


def step_dist(distance):
    return (abs(distance.imag) - distance.real) // 2 + distance.real


def main(text, simple):
    transform = {
        'n': -2j,
        'ne': -1j + 1,
        'se': 1j + 1,
        'nw': -1j - 1,
        'sw': 1j - 1,
        's': 2j,
    }

    moves = [transform[d] for d in text.split(',')]
    history = [step_dist(d) for d in itertools.accumulate(moves)]

    if simple:
        print(history[-1])
    else:
        print(max(history))
