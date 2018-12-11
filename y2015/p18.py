def main(text, simple):
    steps = {dx + 1j * dy for dy in [-1, 0, 1] for dx in [-1, 0, 1]} - {0}

    grid = set()
    for y, row in enumerate(text.splitlines()):
        for x, cell in enumerate(row):
            if cell == '#':
                grid.add(x + 1j * y)

    for _ in range(100):
        new = set()
        for y in range(100):
            for x in range(100):
                p = x + 1j * y
                ns = {p + step for step in steps} & grid
                if p in grid and len(ns) in {2, 3}:
                    new.add(p)
                elif p not in grid and len(ns) == 3:
                    new.add(p)
        grid = new
        if not simple:
            grid |= {0, 99, 99j, 99 + 99j}

    print(len(grid))
