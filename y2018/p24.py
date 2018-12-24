import re
import functools


class Squad:
    pattern = re.compile(
        r'(\d+) units each with (\d+) hit points (\(.+\) |)'
        r'with an attack that does (\d+) (\S+) damage at initiative (\d+)'
    )

    def __init__(self, team, text, boost):
        self.team = team
        match = self.pattern.match(text)
        g = (int(s) if s.isdigit() else s for s in match.groups())
        self.size = next(g)
        self.hp = next(g)
        mods = next(g)
        self.atk = next(g)
        self.type = next(g)
        self.init = next(g)

        unroll = lambda ss: frozenset(w for s in ss for w in s.split(', '))
        self.ims = unroll(re.findall(r'immune to ([^;)]+)', mods))
        self.wks = unroll(re.findall(r'weak to ([^;)]+)', mods))

        # boost
        self.atk += boost if self.team == 0 else 0

    @property
    def power(self):
        return self.size * self.atk

    def attack(self, enemy):
        if self.type in enemy.ims:
            dmg = 0
        else:
            mul = 2 if self.type in enemy.wks else 1
            dmg = self.power * mul
        return dmg

    def defend_from(self, enemy):
        dmg = enemy.attack(self)
        dead = dmg // self.hp
        count = min(self.size, dead)
        msg = f"{enemy} attacks {self}, kills {count}"
        self.size -= dead
        return msg


@functools.lru_cache(maxsize=None)
def simulate(text, boost=0):
    squads = [
        Squad(i, line, boost)
        for i, description in enumerate(text.split('\n\n'))
        for line in description.replace('\n ', ' ').splitlines()[1:]
    ]

    prev = None
    while len({squad.team for squad in squads}) > 1:
        targets = {}

        order = sorted(squads, key=lambda s: (s.power, s.init), reverse=True)
        for squad in order:
            best = None
            for enemy in squads:
                if enemy.team == squad.team:
                    continue
                if enemy in targets.values():
                    continue
                dmg = squad.attack(enemy)
                if dmg:
                    priority = (dmg, enemy.size * enemy.atk, enemy.init)
                    if best is None or priority > best:
                        best = priority
                        targets[squad] = enemy

        for squad in sorted(squads, key=lambda s: s.init, reverse=True):
            if squad.size > 0 and squad in targets:
                targets[squad].defend_from(squad)

        squads = [squad for squad in squads if squad.size > 0]
        pop = sum(squad.size for squad in squads)
        if pop == prev:
            break  # tie
        prev = pop

    victory = {0} == {squad.team for squad in squads}
    return victory, pop


def bsearch(func, lo, hi):
    mid = lo + (hi - lo) // 2
    if lo == mid:
        return hi
    else:
        a = func(lo)[0]
        b = func(mid)[0]
        c = func(hi)[0]
        if a == b:
            return bsearch(func, mid, hi)
        elif b == c:
            return bsearch(func, lo, mid)


def main(text, simple):
    if simple:
        print(simulate(text)[1])
    else:
        boost = bsearch(lambda boost: simulate(text, boost), 0, 100)
        print(simulate(text, boost)[1])
