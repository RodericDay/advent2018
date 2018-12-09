def main(text, simple):
    word_list = [line.split() for line in text.splitlines()]
    if simple:
        valid = lambda words: len(words) == len(set(words))
    else:
        valid = lambda words: len(words) == len(set(map(frozenset, words)))
    print(sum(valid(words) for words in word_list))
