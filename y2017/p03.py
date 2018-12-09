import collections


def main(text, simple):
    n = int(text)

    if simple:
        N = next(i for i in range(10000) if i**2 > n)
        m = (N - 1) // 2
        print(m + m - (N**2 - n))

    else:
        grid = collections.defaultdict(int)
        around = {x + 1j * y for x in [-1, 0, 1] for y in [-1, 0, 1]} - {0}
        p = 0
        for rung in range(999):
            S = 2 * rung  # side length
            steps = [-1j] * (S - 1) + [-1] * (S) + [1j] * (S) + [1] * (S + 1)
            for step in steps:
                grid[p] = sum(grid[p + dp] for dp in around) if p else 1
                if grid[p] > n:
                    print(grid[p])
                    return
                p += step


def display(grid, N):
    half = (N - 1)
    for y in range(-half, half + 1):
        for x in range(-half, half + 1):
            print(f"{grid[x + 1j * y]:<8}", end='')
        print()
