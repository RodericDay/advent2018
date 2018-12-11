def replace(a, b, mol):
    head, *parts = mol.split(a)
    count = mol.count(a)
    for i in range(count):
        replacements = [a] * count
        replacements[i] = b
        yield head + ''.join(r + p for r, p in zip(replacements, parts))


def main(text, simple):
    lines, mol = text.split('\n\n')
    subs = [line.split(' => ') for line in lines.splitlines()]

    if simple:
        print(len({out for a, b in subs for out in replace(a, b, mol)}))

    else:
        count = 0
        while mol != 'e':
            for v, k in subs:
                count += mol.count(k)
                mol = mol.replace(k, v)
        print(count)
