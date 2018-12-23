mapping = {
    "N": -1j,
    "E": 1,
    "S": 1j,
    "W": -1,
}

def main(text, simple):
    if simple:
        return

    text = r'^NNNNNEEEEESS(EEEENNN|WSSSS)EEEEE$'
    # text = r'^NNNNNEEEEESSEEEENNNEEEEE$'

    positions = []
    prev = cur = 0
    distances = {}
    for c in text[1:-1]:
        if c == "(":
            positions.append(cur)
        elif c == ")":
            cur = positions.pop()
        elif c == "|":
            cur = positions[-1]
        else:
            cur += mapping[c]
            if cur not in distances:
                distances[cur] = distances.get(prev, 0) + 1
            else:
                distances[cur] = min(distances[cur], distances[prev] + 1)
        prev = cur

    print(max(distances.values()))
    print(sum(x >= 1000 for x in distances.values()))

    xmin, *_, xmax = sorted(int(p.real) for p in distances)
    ymin, *_, ymax = sorted(int(p.imag) for p in distances)
    screen = '\n'.join(
        ''.join('.' if x + 1j * y in distances else '#'
        for x in range(xmin, xmax + 1))
        for y in range(ymin, ymax + 1))

    print(screen)
