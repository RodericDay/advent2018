import collections


def main(text, simple):
    top = 0
    regs = collections.defaultdict(int)
    for line in text.splitlines():
        _out_, _if_ = line.split(' if ')
        cmd = 'if ' + _if_ + ': ' + _out_.replace('dec', '-=').replace('inc', '+=')
        exec(cmd, None, regs)
        top = max(top, *regs.values())

    if simple:
        print(max(regs.values()))
    else:
        print(top)
