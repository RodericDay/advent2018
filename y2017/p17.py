import collections

def main(text, simple):
    n = int(text)
    i = 0
    l = [0]
    if simple:
        for _ in range(2017):
            i = (i + n) % len(l) + 1
            l.insert(i, len(l))
        print(l[i + 1])
    else:
        for x in range(5 * 10**7):
            i = (i + n) % (x + 1) + 1
            if i == 1:
                ans = x
        print(ans)
