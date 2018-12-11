def knap(N, opts):
    if N == 0:
        yield []
    else:
        for i, o in enumerate(opts):
            if o <= N:
                for tail in knap(N - o, opts[i + 1:]):
                    yield [o] + tail


def main(text, simple):
    if simple:
        return

    containers = sorted([int(n) for n in text.split()], reverse=True)
    item_counts = [len(subset) for subset in knap(150, containers)]
    print(len(item_counts))
    m = min(item_counts)
    print(sum(n == m for n in item_counts))
