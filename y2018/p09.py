import collections


def main(text, simple):
    a, b = [int(n) for n in text.split() if n.isdigit()]
    if not simple:
        b *= 100

    d = collections.deque([0])
    p = collections.Counter()

    for i in range(1, b):
        x = i % a
        if i % 23:
            d.rotate(-1)
            d.append(i)
        else:
            p[x] += i
            d.rotate(7)
            p[x] += d.pop()
            d.rotate(-1)

        # visualize
        # c = collections.deque(d)
        # c.rotate(-c.index(0))
        # print(x, ['*' if n == d[-1] else n for n in c])

    print(p.most_common()[0][1])
