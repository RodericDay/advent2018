import collections

def main(text, simple):
    n = int(text)

    if simple:
        N = next(i for i in range(10000) if i**2 > n)
        m = (N - 1) / 2
        print(m + m - (N**2 - n))

    else:
        N = 5
        grid = collections.defaultdict(int)
        around = {x + 1j*y for x in range(-1, 2) for y in range (-1, 2)} - {0}
        ans = None
        p = 0
        for ring in range(N):
            for step in [-1j] * (2 * ring - 1) + [-1] * (2 * ring) + [1j] * (2 * ring) + [1] * (2 * ring + 1):
                # grid[p] = len(grid) + 1
                grid[p] = sum(grid[p + dp] for dp in around) if len(grid) else 1
                if not ans and grid[p] > n:
                    ans = grid[p]
                p += step

        display(grid, 5)
        print(ans)


def display(grid, N):
    half = (N - 1)
    for y in range(-half, half + 1):
        for x in range(-half, half + 1):
            print(f"{grid[x + 1j * y]:<8}", end='')
        print()
