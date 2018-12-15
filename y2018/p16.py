import re

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

    known, program = text.split('\n\n\n\n')
    seqs = ([int(n) for n in re.findall(r'\d+', line)]
            for line in known.splitlines() if line)
    ans = 0
    possibilities = {i: set(operations) for i in range(len(operations))}
    for before, inst, after in zip(seqs, seqs, seqs):
        r = before
        i, a, b, c = inst
        couldbe = set()
        for kw, op in operations.items():
            copy = r[:]
            copy[c] = op(copy, a, b)
            valid = copy == after
            if valid:
                couldbe.add(kw)

        if len(couldbe) >= 3:
            ans += 1

        possibilities[i] &= couldbe

    d = {}
    while len(d) < len(operations):
        for i, kw in possibilities.items():
            if len(kw) == 1:
                e, = kw
                possibilities.pop(i)
                for k in possibilities.values():
                    k -= {e}
                d[i] = e
                break

    r = [0, 0, 0, 0]
    for line in re.findall(r'(\d+) (\d+) (\d+) (\d+)', program):
        i, a, b, c = map(int, line)
        f = operations[d[i]]
        r[c] = f(r, a, b)

    print(r)
