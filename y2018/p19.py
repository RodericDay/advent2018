operations = {
    "addr": lambda r, a, b: r[a] + r[b],
    "addi": lambda r, a, b: r[a] + b,
    "mulr": lambda r, a, b: r[a] * r[b],
    "muli": lambda r, a, b: r[a] * b,
    "banr": lambda r, a, b: r[a] & r[b],
    "bani": lambda r, a, b: r[a] & b,
    "borr": lambda r, a, b: r[a] | r[b],
    "bori": lambda r, a, b: r[a] | b,
    "setr": lambda r, a, b: r[a],
    "seti": lambda r, a, b: a,
    "gtir": lambda r, a, b: a > r[b],
    "gtri": lambda r, a, b: r[a] > b,
    "gtrr": lambda r, a, b: r[a] > r[b],
    "eqir": lambda r, a, b: a == r[b],
    "eqri": lambda r, a, b: r[a] == b,
    "eqrr": lambda r, a, b: r[a] == r[b],
}

def main(text, simple):
    if simple:
        return
    description, *lines = text.splitlines()

    r = [0 for _ in range(6)]

    def execute(i):
        old = r[:]
        name, *vals = lines[i].split()
        a, b, c = map(int, vals)
        r[c] = int(operations[name](r, a, b))
        if old[0] != r[0]:
            print(''.join(f"{s:<10}" for s in r))

    e = int(next(c for c in description if c.isdigit()))
    r[0] = 0
    while True:
        try:
            execute(r[e])
        except IndexError:
            break
        r[e] += 1

    print(r[0])
