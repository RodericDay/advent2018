def main(text, simple):
    '''
    /r/adventofcode/comments/a53r6i/2018_day_11_solutions/ebjoijs/
    '''
    serial = int(text)
    ints = [n + 1 for n in range(300)]
    G = [[0 for y in range(301)] for x in range(301)]
    S = [[0 for y in range(301)] for x in range(301)]

    for x in ints:
        for y in ints:
            rack = x + 10
            power = rack * y
            power += serial
            power *= rack
            power //= 100
            power %= 10
            power -= 5
            G[x][y] = power

    for x in ints:
        for y in ints:
            S[x][y] = G[x][y] + S[x - 1][y] + S[x][y - 1] - S[x - 1][y - 1]

    best = 0
    best_i = None
    sizes = [3] if simple else ints
    for n in sizes:
        for x in ints[:-n]:
            for y in ints[:-n]:
                total = S[x + n][y + n] - S[x][y + n] - S[x + n][y] + S[x][y]
                if total > best:
                    best = total
                    best_i = (x + 1, y + 1, n)

    print(best_i)
