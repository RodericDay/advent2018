import re


def flatten(node, graph, cache):
    if node not in cache:
        pending = {node}
        seen = set()
        while pending:
            new = {n for p in pending for n in graph[p]}
            pending = new - seen
            seen |= new | pending
        for x in seen:
            cache[x] = frozenset(seen)
    return cache[node]


def main(text, simple):
    graph = {}
    for line in text.splitlines():
        target, *related = map(int, re.findall(r'\d+', line))
        graph[target] = related

    cache = {}
    for node in graph:
        flatten(node, graph, cache)

    if simple:
        print(len(cache[0]))
    else:
        print(len(set(cache.values())))
