import itertools

def main(text, simple):
    stuff = [int(n) for n in text.splitlines()]
    if simple:
        print(sum(stuff))
        return
    seen = set()
    for n in itertools.accumulate(itertools.cycle(stuff)):
        if n in seen:
            print(n)
            return
        seen.add(n)
