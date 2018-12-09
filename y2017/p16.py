def p(a, b):
    def f(dancers):
        i, j = dancers.index(a), dancers.index(b)
        dancers[i], dancers[j] = b, a
    return f


def x(a, b):
    a, b = int(a), int(b)

    def f(dancers):
        dancers[a], dancers[b] = dancers[b], dancers[a]
    return f


def s(a):
    a = int(a)

    def f(dancers):
        dancers[:] = dancers[-a:] + dancers[:-a]
    return f


def spin(moves, dancers):
    dancers = list(dancers)
    for move in moves:
        move(dancers)
    return ''.join(dancers)


def main(text, simple, cache={}):
    dancers = ''.join(chr(ord('a') + i) for i in range(16))
    moves = [eval(move[0])(*move[1:].split('/')) for move in text.split(',')]

    while dancers not in cache:
        cache[dancers] = len(cache)
        dancers = spin(moves, dancers)

    if simple:
        print(list(cache)[0])
    else:
        print(list(cache)[10**9 % len(cache)])
