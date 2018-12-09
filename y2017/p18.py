import collections


def program(text, pid, qrcv, qsnd):
    lines = text.splitlines()
    r = collections.defaultdict(int)
    r['p'] = pid
    i = 0
    rcv_count = 0
    while i < len(lines):
        line = lines[i]
        i += 1

        f, X, *Y = line.split()
        if X.strip('-').isdigit():
            r[X] = int(X)
        if Y:
            Y = Y[0]
            if Y.strip('-').isdigit():
                r[Y] = int(Y)

        if f == 'set':
            r[X] = r[Y]
        elif f == 'add':
            r[X] += r[Y]
        elif f == 'mul':
            r[X] *= r[Y]
        elif f == 'mod':
            r[X] %= r[Y]
        elif f == 'jgz':
            if r[X] > 0:
                i += r[Y] - 1  # take back the step taken
        elif f == 'snd':
            qsnd.append(r[X])
        elif f == 'rcv':
            if qrcv is qsnd:
                if r[X] != 0:
                    yield qrcv[-1]

            else:
                while len(qrcv) <= rcv_count:
                    yield 'wait'
                r[X] = qrcv[rcv_count]
                rcv_count += 1
                yield 'send'


def main(text, simple):
    if simple:
        q = []
        p = program(text, 0, q, q)
        print(next(p))

    else:
        q0, q1 = [], []
        p0 = program(text, 0, q1, q0)
        p1 = program(text, 1, q0, q1)
        for s0, s1 in zip(p0, p1):
            if {s0, s1} == {'wait'}:
                break
        print(len(q1))
