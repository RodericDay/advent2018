import re


def main(text, simple):

    def is_nice(string):
        if simple:
            yield len(re.findall(r'[aeiou]', string)) >= 3
            yield re.findall(r'(.)\1', string)
            yield not re.findall(r'(ab|cd|pq|xy)', string)
        else:
            yield re.findall(r'(..).*\1', string)
            yield re.findall(r'(.).\1', string)

    print(sum(all(is_nice(line)) for line in text.splitlines()))
