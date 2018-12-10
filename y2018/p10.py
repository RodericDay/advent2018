import itertools
import re


def point(px, py, vx, vy):
    while True:
        yield px, py
        px += vx
        py += vy


def main(text, simple):
    if simple:
        return

    lines = text.splitlines()
    points = [point(*map(int, re.findall(r'-?\d+', line))) for line in lines]
    smallest = 100
    for tic in itertools.count():
        seen = {next(p) for p in points}
        xmin, *_, xmax = sorted(p[0] for p in seen)
        ymin, *_, ymax = sorted(p[1] for p in seen)

        width = xmax - xmin
        if width < smallest:
            smallest = width
            screen = str(tic)
            for y in range(ymin, ymax + 1):
                screen += '\n'
                for x in range(xmin, xmax + 1):
                    v = '#' if (x, y) in seen else ' '
                    screen += v

        if width < 100 and width > smallest:
            print(screen)
            return
