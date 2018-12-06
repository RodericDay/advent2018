def main(text, simple):
    if not simple:
        return
    grid = {}
    for y, line in enumerate(text.splitlines()):
        for x, cell in enumerate(line):
            if cell != ' ':
                grid[x + 1j * y] = cell

    pos = min(grid, key=lambda n: n.imag)
    vel = 1j
    letters = ''
    steps = 0
    while pos in grid:
        steps += 1
        if grid[pos].isalpha():
            letters += grid[pos]
        if grid[pos] == '+':
            for turn in [-1j, 1j]:
                new = grid.get(pos + vel * turn)
                a = new == '-' and (vel * turn).imag == 0
                b = new == '|' and (vel * turn).real == 0
                if a or b:
                    vel *= turn
        pos += vel
    print(letters)
    print(steps)
