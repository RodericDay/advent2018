import itertools

shop1 = '''
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
'''

shop2 = '''
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
'''

shop3 = '''
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''


def outcome(p_hp, p_atk, p_def, b_hp, b_atk, b_def):
    while True:
        b_hp -= max(1, p_atk - b_def)
        if b_hp <= 0:
            return True
        p_hp -= max(1, b_atk - p_def)
        if p_hp <= 0:
            return False


def main(text, simple):
    if simple:
        return

    get3int = lambda text: [int(n) for n in text.split() if n.isdigit()][-3:]

    b_hp, b_atk, b_def = get3int(text)
    weapons = [combo for combo in map(get3int, shop1.splitlines()) if combo]
    armors = [combo for combo in map(get3int, shop2.splitlines()) if combo]
    rings = [combo for combo in map(get3int, shop3.splitlines()) if combo]

    nothing = (0, 0, 0)
    armors += [nothing]
    rings += [nothing]

    loadouts = {}
    for w, a, r1, r2 in itertools.product(weapons, armors, rings, rings):
        if r1 is r2 and r1 is not nothing:
            continue

        lt = cost, atk_up, def_up = tuple(sum(g) for g in zip(w, a, r1, r2))
        if lt not in loadouts:
            loadouts[lt] = outcome(100, atk_up, def_up, b_hp, b_atk, b_def)

    print(min(k for k, v in loadouts.items() if v)[0])
    print(max(k for k, v in loadouts.items() if not v)[0])
