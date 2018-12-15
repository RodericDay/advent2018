def main(text, simple):
    elves, a, b = [3, 7], 0, 1

    if simple:
        goal = int(text)
        condition = lambda: len(elves) <= goal + 10
    else:
        N = len(text)
        digits = [int(n) for n in text]
        condition = lambda: elves[-N:] != digits and elves[-N - 1:-1] != digits

    while condition():
        total = elves[a] + elves[b]
        elves += [total // 10, total % 10] if total >= 10 else [total]
        a = (a + elves[a] + 1) % len(elves)
        b = (b + elves[b] + 1) % len(elves)

    if simple:
        print(''.join(str(n) for n in elves[goal:goal + 10]))
    else:
        print(len(elves) - len(text))
