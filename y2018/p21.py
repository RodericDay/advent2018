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

    def execute(i, seen=set()):
        old = r[:]
        name, *vals = lines[i].split()
        a, b, c = map(int, vals)
        r[c] = int(operations[name](r, a, b))
        if r[e] == 28:
            state = ''.join(f"{s:<15}" for s in r)
            if r[4] in seen:
                raise RuntimeError
            seen.add(r[4])
            print(state)


    e = int(next(c for c in description if c.isdigit()))
    r[0] = 3

    while True:
        execute(r[e])
        r[e] += 1
