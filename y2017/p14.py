from y2017.p10 import knot_hash


def connected_components(grid, mov={1, -1, 1j, -1j}):
    groups = []
    while grid:
        pending = {grid.pop()}
        seen = set()
        while pending:
            seen |= pending
            grid -= pending
            pending = {pos + step for pos in pending for step in mov} & grid
        groups.append(seen)
    return groups


def main(text, simple):
    grid = set()
    for y in range(128):
        row = ''.join(f"{int(c, 16):0>4b}" for c in knot_hash(f"{text}-{y}"))
        for x, v in enumerate(row):
            if v == '1':
                grid.add(x + 1j * y)

    if simple:
        print(len(grid))
    else:
        components = connected_components(grid)
        print(len(components))
