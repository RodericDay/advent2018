import re
import collections

def particle(px, py, pz, vx, vy, vz, ax, ay, az):
    while True:
        vx += ax
        vy += ay
        vz += az
        px += vx
        py += vy
        pz += vz
        yield px, py, pz

def main(text, simple):
    particles = [
        [int(n) for n in re.findall(r'-?\d+', line)]
        for line in text.splitlines()
    ]

    if simple:
        print(min((sum(abs(n) for n in p[-3:]), sum(abs(n) for n in p[:3]), i) for i, p in enumerate(particles))[2])
    else:
        gs = [particle(*p) for p in particles]
        for iteration in range(100):
            seen = collections.defaultdict(list)
            for i, g in enumerate(gs):
                seen[next(g)].append(i)
            gs = [gs[vs[0]] for k, vs in seen.items() if len(vs) == 1]
        print(len(gs))
