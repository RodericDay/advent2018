def main(text, simple):
    if simple:
        print(sum(len(words) == len(set(words)) for line in text.splitlines() for words in [line.split()]))
    else:
        print(sum(len(words) == len(set(map(frozenset, words))) for line in text.splitlines() for words in [line.split()]))
