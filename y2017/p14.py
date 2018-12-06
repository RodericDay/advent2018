from y2017.p10 import knot_hash


def connected_components(grid, mov={1, -1, 1j, -1j}):
    groups = []
    while grid:
        active = {grid.pop()}
        seen = set()
        while active:
            seen |= active
            grid -= active
            active = {pos + step for pos in active for step in mov if pos + step in grid}
        groups.append(seen)
    return groups


def main(text, simple):
    grid = set()
    for y in range(128):
        for x, v in enumerate(''.join(f"{int(c, 16):0>4b}" for c in knot_hash(f"{text}-{y}"))):
            if v == '1':
                grid.add(x + 1j * y)

    if simple:
        print(len(grid))
    else:
        components = connected_components(grid)
        print(len(components))
