import re
import collections


def main(text, simple):
    if simple:
        return

    d, X, Y = [int(e) for e in re.findall(r'\d+', text)]

    graph = {}
    for y in range(2 * Y):
        for x in range(2 * X):
            p = x + 1j * y
            if x == 0 and y == 0:
                v = d % 20183
            elif y == 0:
                v = (x * 16807 + d) % 20183
            elif x == 0:
                v = (y * 48271 + d) % 20183
            else:
                v = (graph[p - 1] * graph[p - 1j] + d) % 20183
            graph[p] = v
    graph[X + 1j * Y] = 0
    graph = {k: v % 3 for k, v in graph.items()}

    print(sum(v for p, v in graph.items() if p.real <= X if p.imag <= Y))

    equipment = ['tc', 'cn', 'nt']

    sequence = collections.deque([(0, 't', 0)])
    costs = {(0, 't'): 0}
    goal = X + 1j * Y
    while sequence:
        p0, e0, c0 = sequence.pop()
        toggle = equipment[graph[p0]]
        for step in [0, 1, -1, 1j, -1j]:
            if step:
                p1, e1 = p0 + step, e0
                c1 = 1 + c0
            else:
                p1, e1 = p0, toggle[e0 == toggle[0]]
                c1 = 7 + c0
            if c1 + abs(X - p1.real) + abs(Y - p1.imag) < 1.4 * (X + Y):
                if p1 in graph:
                    if e1 in equipment[graph[p1]]:
                        best = costs.get((p1, e1), float('inf'))
                        if c1 < best:
                            costs[p1, e1] = c1
                            sequence.appendleft((p1, e1, c1))

    print(costs[goal, 't'])
