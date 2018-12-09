import collections
import re


def main(text, simple):
    backward = {}
    forward = {}
    weight = {}
    for line in text.splitlines():
        info, *rest = line.split(' -> ')
        parent = info.split()[0]
        children = rest[0].split(', ') if rest else []
        for child in children:
            backward[child] = parent
        forward[parent] = children
        weight[parent] = int(re.findall(r'\d+', info)[0])

    base, = set(forward) - set(backward)
    if simple:
        print(base)
        return

    def total_weight(name, cache={}):
        if name not in cache:
            extra = sum(total_weight(name) for name in forward[name])
            cache[name] = weight[name] + extra
        return cache[name]

    def odd_one_out(name):
        d = collections.defaultdict(list)
        for c in forward[name]:
            d[total_weight(c)].append(c)
        odd, normal = sorted(d, key=lambda k: len(d[k]))
        offset = normal - odd
        return d[odd][0], offset

    for i in range(10):
        try:
            base, offset = odd_one_out(base)
        except ValueError:
            print(weight[base] + offset)
            break
