def main(text, simple):
    seen = {}
    banks = [int(n) for n in text.split()]

    c = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = c
        c += 1
        m = max(banks)
        i = banks.index(m)
        banks[i] = 0
        while m:
            m -= 1
            i = (i + 1) % len(banks)
            banks[i] += 1

    if simple:
        print(c)
    else:
        print(c - seen[tuple(banks)])
