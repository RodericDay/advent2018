import collections
import re


def main(text, simple):
    tasks_left = set()
    requirements = collections.defaultdict(set)
    for line in text.splitlines():
        A, B = re.findall(r'([A-Z]) ', line)
        tasks_left |= {A, B}
        requirements[B].add(A)

    if simple:
        work_left = {t: 1 for t in tasks_left}
        workers = {0: None}
    else:
        work_left = {t: 60 + ord(t) - ord('A') + 1 for t in tasks_left}
        workers = {i: None for i in range(5)}

    C = 0
    M = ''
    while tasks_left:
        tasks_available = sorted([
            t for t in tasks_left
            if not requirements[t]
            if t not in workers.values()
        ], reverse=True)

        for i in workers:
            if workers[i] is None and tasks_available:
                workers[i] = tasks_available.pop()
            if workers[i]:
                task = workers[i]
                if work_left[task]:
                    work_left[task] -= 1
                if not work_left[task]:
                    workers[i] = None
                    M += task

        tasks_left = {t for t, w in work_left.items() if w != 0}
        for r in requirements.values():
            r &= tasks_left
        C += 1

    if simple:
        print(M)
    else:
        print(C)
