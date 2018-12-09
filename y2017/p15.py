def f(n, A, D):
    while True:
        n = (n * A) % D
        yield n


def main(text, simple):
    A, B = [int(line.split()[-1]) for line in text.splitlines()]
    gA = f(A, 16807, 2147483647)
    gB = f(B, 48271, 2147483647)
    S = 2 ** 16 - 1

    if simple:
        print(sum(next(gA) & S == next(gB) & S for _ in range(40 * 10**6)))

    else:
        ggA = (n for n in gA if n % 4 == 0)
        ggB = (n for n in gB if n % 8 == 0)
        print(sum(next(ggA) & S == next(ggB) & S for _ in range(5 * 10**6)))
