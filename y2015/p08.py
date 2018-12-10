import json


def main(text, simple):
    lines = text.splitlines()
    if simple:
        print(sum(len(line) - len(eval(line)) for line in lines))
    else:
        print(sum(len(json.dumps(line)) - len(line) for line in lines))
