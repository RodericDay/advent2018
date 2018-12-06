def main(text, simple):
    depth = eval('{' + text.replace('\n', ',\n') + '}')

    if simple:
        print(sum(i * d for i, d in depth.items() if (i % (2 * d - 2)) == 0))

    else:
        for delay in range(10000000):
            if all(0 != (delay + i) % (2 * d - 2) for i, d in depth.items()):
                print(delay)
                return
