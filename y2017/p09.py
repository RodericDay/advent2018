import re


def score(thing, prev=0):
    if thing is None:
        return 0
    return 1 + prev + sum(score(sub, prev + 1) for sub in thing)


def main(text, simple):
    count = 0
    def cleaner(match):
        nonlocal count
        count += len(match.group(1))
        return 'None'

    text = re.sub(r'!.', '', text)
    text = re.sub(r'<([^>]*?)>', cleaner, text)
    text = text.replace('{','[').replace('}',']')

    if simple:
        print(score(eval(text)))
    else:
        print(count)
