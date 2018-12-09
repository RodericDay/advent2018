import collections
import datetime
import re


def main(text, simple):
    lines = sorted(text.splitlines())
    periods = collections.defaultdict(list)
    for line in lines:
        y, m, d, H, M, *label = map(int, re.findall(r'\d+', line))
        if label:
            guard = label[0]
        else:
            date = datetime.datetime(y, m, d, H, M)
            periods[guard].append(date)

    total = collections.Counter()
    freqs = collections.defaultdict(lambda: collections.Counter())
    for guard, ps in periods.items():
        g = iter(ps)
        for a, b in zip(g, g):
            total[guard] += (b - a).total_seconds()
            minutes = int((b - a).total_seconds() / 60)
            freqs[guard].update((a.minute + n) % 60 for n in range(minutes))

    if simple:
        k = max(total, key=lambda k: total[k])
        print(k * freqs[k].most_common()[0][0])
    else:
        d = {n: m * gid for gid, C in freqs.items() for m, n in C.items()}
        print(d[max(d)])
