def main(text, simple):
    boxes = [[int(n) for n in line.split('x')] for line in text.splitlines()]
    if simple:
        paper = lambda a, b, c: 2 * a * b + 2 * b * c + 2 * a * c + a * b
        print(sum(paper(*sorted(box)) for box in boxes))
    else:
        ribbon = lambda a, b, c: 2 * a + 2 * b + a * b * c
        print(sum(ribbon(*sorted(box)) for box in boxes))
