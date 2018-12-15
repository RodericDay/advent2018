import collections


steps = [-1j, -1, 1, 1j]
near = lambda p: (p + step for step in steps)
reading_order = lambda p: (p.imag, p.real)


def viz(units):
    global grid
    xmax = max(int(p.real) for p in grid) + 2
    ymax = max(int(p.imag) for p in grid) + 2
    state = ''
    for y in range(ymax):
        state += '\n' if y else ''
        for x in range(xmax):
            p = x + 1j * y
            state += units.get(p) or (' ' if p in grid else '#')
    return state


def next_step(start, ends, grid):
    unexplored = collections.deque([start])
    explored = {}  # and first parent
    while unexplored:
        p = unexplored.pop()
        if p in ends:
            while p not in near(start):
                p = explored[p]
            return p
        for n in near(p):
            if n in grid:
                if n not in explored:
                    explored[n] = p
                    unexplored.appendleft(n)


def main(text, simple):
    global grid

    if simple:
        return

    grid = set()
    units = {}
    health = {}

    # init
    for y, row in enumerate(text.strip().splitlines()):
        for x, cell in enumerate(row):
            if cell != '#':
                p = x + 1j * y
                grid.add(p)
                if cell != '.':
                    units[p] = cell
                    health[p] = 200

    elf_start = sum(unit == 'E' for unit in units.values())
    state = text, sum(health.values())
    record = {}

    rounds = 0
    while state not in record:
        record[state] = len(record)

        took_turn = set()
        for p in sorted(units, key=reading_order):

            if p not in units:  # dead
                continue

            if p in took_turn:  # standing on corpse!
                continue

            enemies = {u for u in units if units[p] != units[u]}
            if len(enemies) == 0:  # game over!
                break

            # movement
            accessible = near(p)
            near_enemies = {n for e in enemies for n in near(e)}
            if not set(near(p)) & enemies:
                q = next_step(p, near_enemies, grid - set(units))
                if q:
                    units[q] = units.pop(p)
                    health[q] = health.pop(p)
                    p = q

            # attack
            targets = set(near(p)) & enemies
            if targets:
                t = min(targets, key=lambda t: (health[t], reading_order(t)))
                health[t] -= 3 if units[p] == 'G' else 16
                if health[t] <= 0:
                    units.pop(t)
                    health.pop(t)

            took_turn.add(p)

        else:  # nobreak
            rounds += 1

        state = viz(units), sum(health.values())

    elf_end = sum(unit == 'E' for unit in units.values())
    final_state = max(record, key=record.get)
    print(final_state[0])
    print(rounds, final_state[1])
    score = rounds * final_state[1]
    print(score)
    print(elf_start, elf_end)
    return score
