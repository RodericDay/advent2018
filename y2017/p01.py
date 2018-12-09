def main(text, simple):
    ns = [int(n) for n in text]
    N = len(ns)
    if simple:
        print(sum(ns[i] for i in range(N) if ns[i] == ns[i - 1]))
    else:
        print(sum(ns[i] for i in range(N) if ns[i] == ns[i - N // 2]))
