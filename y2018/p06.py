import collections

def main(text, simple):
    grid = set()
    for line in text.splitlines():
        x, y = map(int, line.split(', '))
        grid.add(x + 1j * y)
    grid = list(grid)

    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)

    if simple:
        counter = collections.defaultdict(set)
        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                p = x + 1j * y
                a, b, *_ = sorted((abs(d.imag) + abs(d.real), i) for i, n in enumerate(grid) for d in [p - n])
                if a[0] != b[0]:
                    u = a[1]
                    counter[u].add(x + 1j * y)
        print(len(max(counter.values(), key=len)))

    else:
        count = 0
        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                p = x + 1j * y
                t = sum((abs(d.imag) + abs(d.real)) for n in grid for d in [p - n])
                if t < 10000:
                    count += 1
        print(count)
