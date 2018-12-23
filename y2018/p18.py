import collections


def viz(state):
    for y in range(10):
        for x in range(10):
            p = x + 1j * y
            print(state[p], end='')
        print()
    print()


def main(text, simple):
    if simple:
        return

    state = {}
    for y, row in enumerate(text.splitlines()):
        for x, cell in enumerate(row):
            p = x + 1j * y
            state[p] = cell
    valid = set(state)

    steps = {a + b for a in [1, 0, -1] for b in [1j, 0, -1j]} - {0}
    near = lambda p: {p + s for s in steps} & valid

    seen = {}
    counted = {}
    while True:
        hashed = frozenset(state.items())
        if hashed in seen:
            print(len(seen), seen[hashed])
            break
        seen[hashed] = len(counted)
        counted[len(counted)] = state

        new_state = {}
        for p, v in state.items():
            c = collections.Counter(state[n] for n in near(p))
            if v == '.' and c['|'] >= 3:
                new_state[p] = '|'
            elif v == '|' and c['#'] >= 3:
                new_state[p] = '#'
            elif v == '#' and c['#'] >= 1 and c['|'] >= 1:
                new_state[p] = '#'
            elif v == '|':
                new_state[p] = '|'
            else:
                new_state[p] = '.'
        state = new_state

    final = counted[(1000000000 - 460) % (460 - 432) + 432]
    c = collections.Counter(final.values())
    print(c['|'] * c['#'])
