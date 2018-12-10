import collections
import re


def run(code, r):
    instructions = collections.deque(code.splitlines())
    while instructions:
        try:
            exec(instructions[-1], {}, r)
            instructions.pop()
        except NameError:
            instructions.rotate(1)
    return r['A']


def main(text, simple):
    if simple:
        return

    code = (
        re.sub(r'(.+?) -> (.+)', r'\2 = \1', text)
        .replace('RSHIFT', '>>')
        .replace('LSHIFT', '<<')
        .replace('AND', '&')
        .replace('OR', '|')
        .replace('NOT ', '~')
    ).upper()

    A = run(code, {})
    print(A)

    code = re.sub(r'^B =.+\n', '', code, flags=re.MULTILINE)
    print(run(code, {'B': A}))
