import collections
import re


def main(text, simple):
    if simple:
        return

    initial, *pairs = re.findall(r'[.#]+', text)
    mapping = {a: b for a, b in zip(pairs[::2], pairs[1::2])}

    pots = collections.defaultdict(lambda: '.')
    pots.update({i: v for i, v in enumerate(initial)})

    seen = set()
    for n in range(1000):
        span = range(min(pots) - 5, max(pots) + 5)

        if n == 20:
            print(sum(i for i, v in pots.items() if v == '#'))

        pattern = ''.join(pots[i] for i in span).strip('.')
        if pattern in seen:
            N = 50000000000
            print(sum(i + (N - n) for i, v in pots.items() if v == '#'))
            return
        seen.add(pattern)

        new = {
            i: mapping.get(window, '.')
            for i in span
            for window in [''.join(pots[i + j] for j in range(-2, 3))]
        }
        pots.clear()
        pots.update(new)
