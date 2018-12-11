import re


def main(text, simple):
    known = '''
        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1
    '''

    finder = re.compile(r"(\w+): (\d+)")
    parse = lambda line: {k: int(v) for k, v in finder.findall(line)}
    real_sue = parse(known)
    sues = [parse(sue) for sue in text.splitlines()]

    def compare(sue):
        for k, v in sue.items():
            if not simple and k in {'cats', 'trees'}:
                yield sue[k] > real_sue[k]
            elif not simple and k in {'pomeranians', 'goldfish'}:
                yield sue[k] < real_sue[k]
            else:
                yield sue[k] == real_sue[k]

    print(next(i + 1 for i, sue in enumerate(sues) if all(compare(sue))))
