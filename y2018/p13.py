def tic(p, cars, grid):
    v, c = cars.pop(p)
    tile = grid[p]

    # I wish Python had cases like Haskell :/
    _ = None
    if False: pass  # noqa
    elif (tile, v, _) == ('/' ,  1 , _): v, c =     -1j, c  # noqa
    elif (tile, v, _) == ('/' , -1j, _): v, c =      1 , c  # noqa
    elif (tile, v, _) == ('/' , -1 , _): v, c =      1j, c  # noqa
    elif (tile, v, _) == ('/' ,  1j, _): v, c =     -1 , c  # noqa
    elif (tile, v, _) == ('\\',  1 , _): v, c =      1j, c  # noqa
    elif (tile, v, _) == ('\\',  1j, _): v, c =      1 , c  # noqa
    elif (tile, v, _) == ('\\', -1 , _): v, c =     -1j, c  # noqa
    elif (tile, v, _) == ('\\', -1j, _): v, c =     -1 , c  # noqa
    elif (tile, _, c) == ('+' ,  _ , 0): v, c = v * -1j, (c + 1) % 3  # noqa
    elif (tile, _, c) == ('+' ,  _ , 1): v, c = v *  1 , (c + 1) % 3  # noqa
    elif (tile, _, c) == ('+' ,  _ , 2): v, c = v *  1j, (c + 1) % 3  # noqa

    if p + v in cars:
        # crash!
        if len(cars) == 16:
            print(p + v)
        cars.pop(p + v)
    else:
        cars[p + v] = (v, c)


def main(text, simple):
    if simple:
        return

    cars = {}
    grid = {}
    for y, row in enumerate(text.splitlines()):
        for x, glyph in enumerate(row):
            if glyph.strip():
                p = x + 1j * y

                if glyph == '>':
                    cars[p] = (1, 0)
                    glyph = '-'

                elif glyph == '<':
                    cars[p] = (-1, 0)
                    glyph = '-'

                elif glyph == '^':
                    cars[p] = (-1j, 0)
                    glyph = '|'

                elif glyph == 'v':
                    cars[p] = (1j, 0)
                    glyph = '|'

                grid[p] = glyph

    while len(cars) > 1:
        order = sorted(cars, key=lambda p: (p.imag, p.real))
        for p in order:
            if p in cars:
                tic(p, cars, grid)

    last, = cars
    print(last)
