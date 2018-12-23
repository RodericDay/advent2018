import re


def init(text):
    rin = r'(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)'
    rout = r'\1s = [\2]; \3s = range(\4, \5 + 1)'
    tiles = {}
    for line in text.splitlines():
        exec(re.sub(rin, rout, line), {}, globals())
        for y in ys:
            for x in xs:
                tiles[x + 1j * y] = '#'
    return tiles


def viz(tiles):
    xmin, *_, xmax = sorted(int(p.real) for p in tiles)
    ymin, *_, ymax = sorted(int(p.imag) for p in tiles)
    xs = range(xmin, xmax + 2)
    ys = range(ymin, ymax + 1)
    tile = lambda p: tiles.get(p, ' ')
    screen = '\n'.join(''.join(tile(x + 1j * y) for x in xs) for y in ys)

    print(screen.count('.'))
    with open("p17dump.txt", "w") as fp:
        fp.write(screen)


def flow(start, D=1):
    # add water by DFSing downwards
    stack = [start]
    water = {}
    while stack and stack[-1].imag <= lim:
        p = stack.pop()
        water[p] = '.'
        for s in [D, -D, 1j]:
            n = p + s
            if n not in tiles:
                if n not in water:
                    stack.append(n)

    # recover all the paths not traveled, by finding wanting nodes
    for p in list(water):
        if p - D in water and p - 1j in water and p - D - 1j not in water:
            while p + D not in tiles and p + D not in water:
                p += D
                water[p] = '.'
                if p + 1j not in water and p + 1j not in tiles:
                    water.update(flow(p))
                    break

    return water


def drain(tiles):
    # remove flowing water by DFSing from every sink upwards
    lim = max(p.imag for p in tiles)
    seq = [p for p in water if tiles[p] == '.' and p.imag == lim]
    while seq:
        p = seq.pop()
        tiles.pop(p)
        for s in [-1, 1, -1j]:
            n = p + s
            if tiles.get(n) == '.':
                seq.append(n)


with open("p17.txt") as fp:
    text = fp.read()

tiles = init(text)

lim = max(p.imag for p in tiles)

water = flow(500)

tiles = {**tiles, **water}

viz(tiles)

drain(tiles)

viz(tiles)
