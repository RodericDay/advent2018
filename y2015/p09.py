import itertools


def main(text, simple):
    if simple:
        return

    destinations = set()
    graph = {}
    for line in text.splitlines():
        A, _, B, _, d = line.split()
        destinations |= {A, B}
        graph[A + B] = int(d)
        graph[B + A] = int(d)

    routes = [
        sum(graph[a + b] for a, b in zip(combo, combo[1:]) if a + b in graph)
        for combo in itertools.permutations(destinations)
    ]

    print(min(routes))
    print(max(routes))
