import itertools
import re


def main(text, simple):
    graph = {}
    people = set()
    for line in text.splitlines():
        a, delta, n, b = re.findall(r'([A-Z][a-z]+|\d+|gain|lose)', line)
        graph[a + b] = int(n) * (1 if delta == 'gain' else -1)
        people |= {a, b}

    if not simple:
        people.add('Me')

    happiness = (
        sum(
            graph.get(a + b, 0) + graph.get(b + a, 0)
            for a, b in zip(seq, seq[1:] + seq[:1])
        ) for seq in itertools.permutations(people)
    )

    print(max(happiness))
