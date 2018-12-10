import re


def reindeer(string):
    v, dt, rt = map(int, re.findall(r'\d+', string))
    distance = 0
    stamina = dt
    rest = rt
    while True:
        if stamina:
            distance += v
            yield distance
            stamina -= 1
        elif rest:
            yield distance
            rest -= 1
        else:
            stamina = dt
            rest = rt


def main(text, simple):
    if simple:
        return

    deers = [reindeer(line) for line in text.splitlines()]

    points = [0 for _ in deers]
    for t in range(2503):
        traveled = [next(r) for r in deers]
        lead = max(traveled)
        points = [p + (d == lead) for p, d in zip(points, traveled)]

    print(max(traveled))
    print(max(points))
