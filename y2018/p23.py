import collections
import re
import itertools
import math


def in_range_of(b1, b2):
    ax, ay, az, ar = b1
    bx, by, bz, *_ = b2
    return abs(ax - bx) + abs(ay - by) + abs(az - bz) <= ar


def main(text, simple):
    if simple:
        return

    bots = []
    for line in text.splitlines():
        x, y, z, r = [int(n) for n in re.findall(r'-?\d+', line)]
        bots.append([x, y, z, r])

    best_bot = max(bots, key=lambda t: t[-1])
    print(sum(in_range_of(best_bot, bot) for bot in bots))

    xs, ys, zs, _ = [[min(seq), max(seq) + 1] for seq in zip(*bots)]
    res = 2 ** math.ceil(math.log(max(xs) - min(xs), 2))

    closest_dist = float('inf')
    while res > 0:
        highest_count = 0
        xs = range(min(xs), max(xs), res)
        ys = range(min(ys), max(ys), res)
        zs = range(min(zs), max(zs), res)
        for point in itertools.product(xs, ys, zs):
            count = sum(in_range_of(bot, point) for bot in bots)
            dist_to_origin = sum(abs(n) for n in point)
            if count > highest_count:
                highest_count = count
                closest_dist = dist_to_origin
                closest_point = point
            elif count == highest_count and dist_to_origin < closest_dist:
                closest_dist = dist_to_origin
                closest_point = point
        xs, ys, zs = [[d - res, d + res + 1] for d in closest_point]
        res //= 2
    print(closest_dist)
