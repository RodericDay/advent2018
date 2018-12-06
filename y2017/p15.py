def f(n, A, D):
    while True:
        yield n
        n = n * A % D

def main(text, simple):
    A, B = [int(line.split()[-1]) for line in text.splitlines()]
    gA = f(A, 16807, 2147483647)
    gB = f(B, 48271, 2147483647)

    if simple:
        print(sum(f"{next(gA):b}"[-16:] == f"{next(gB):b}"[-16:] for _ in range(40 * 10**6)))

    else:
        ggA = (n for n in gA if n % 4 == 0)
        ggB = (n for n in gB if n % 8 == 0)
        print(sum(f"{next(ggA):b}"[-16:] == f"{next(ggB):b}"[-16:] for _ in range(5 * 10**6)))
