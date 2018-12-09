import re


def reduct(text):
    diff = ord('a') - ord('A')

    i = 0
    while i < len(text) - 1:
        if abs(ord(text[i]) - ord(text[i + 1])) == diff:
            text = text[:i] + text[i + 2:]
            i = max(i - 1, 0)
        else:
            i += 1

    return text


def main(text, simple):
    if simple:
        print(len(reduct(text)))
    else:
        text = reduct(text)
        unique = set(text.lower())
        subs = [re.sub(c, '', text, flags=re.IGNORECASE) for c in unique]
        print(len(min(map(reduct, subs), key=len)))
