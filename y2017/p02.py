def main(text, simple):
    sheet = [[int(n) for n in line.split()] for line in text.splitlines()]
    if simple:
        print(sum(max(line) - min(line) for line in sheet))
    else:
        divs = lambda line: (a / b for a in line for b in line)
        print(sum(int(n) for line in sheet for n in divs(line) if not n % 1))
