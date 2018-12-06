def main(text, simple):
    steps = [int(n) for n in text.split()]
    i = c = 0
    while True:
        if i >= len(steps):
            break
        c += 1
        delta = 1 if simple else (1 if steps[i] < 3 else -1)
        steps[i] += delta
        i += steps[i] - delta
    print(c)
