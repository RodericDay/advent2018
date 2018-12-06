import re
import collections
import datetime

def main(text, simple):
    periods = collections.defaultdict(list)
    lines = text.splitlines()
    for line in sorted(lines):
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
            freqs[guard].update([n % 60 for n in range(a.minute, a.minute + int((b - a).total_seconds() // 60))])

    if simple:
        k = max(total, key=lambda k: total[k])
        print(k * freqs[k].most_common()[0][0])
    else:
        a, b, c = max((n, m, k) for k, C in freqs.items() for m, n in C.most_common())
        print(b * c)
