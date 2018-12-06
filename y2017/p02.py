def main(text, simple):
    sheet = [[int(n) for n in line.split('\t')] for line in text.splitlines()]
    if simple:
        print(sum(max(line) - min(line) for line in sheet))
    else:
        print(sum([b // a for a in line for b in line if b > a and b / a % 1 == 0][0] for line in sheet))
