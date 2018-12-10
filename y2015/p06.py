import collections
import re


def main(text, simple):
    if simple:
        return

    grid1 = collections.defaultdict(bool)
    grid2 = collections.defaultdict(int)
    for line in text.splitlines():
        action, = re.findall(r'(on|off|toggle)', line)
        ax, ay, bx, by = map(int, re.findall(r'\d+', line))
        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                p = (x, y)
                if action == 'off':
                    grid1[p] = False
                    grid2[p] = max(0, grid2[p] - 1)
                elif action == 'on':
                    grid1[p] = True
                    grid2[p] += 1
                elif action == 'toggle':
                    grid1[p] = not grid1[p]
                    grid2[p] += 2

    print(sum(n for n in grid1.values()))
    print(sum(n for n in grid2.values()))
