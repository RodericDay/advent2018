def main(text, simple):
    ns = [int(n) for n in text]
    if simple:
        print(sum(ns[i] for i in range(len(ns)) if ns[i] == ns[i - 1]))
    else:
        print(sum(ns[i] for i in range(len(ns)) if ns[i] == ns[i - len(ns)//2]))
