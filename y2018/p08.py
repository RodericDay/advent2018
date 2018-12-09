import collections


Tree = collections.namedtuple("Tree", "children meta")


def main(text, simple):
    if simple:
        # text = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        data = [int(n) for n in text.split()][::-1]
        tree, _ = parse(data)
        print(sum_meta(tree))
        print(sum_real(tree))


def sum_meta(tree):
    return sum(tree.meta + [sum_meta(leaf) for leaf in tree.children])


def sum_real(tree):
    if not tree.children:
        return sum(tree.meta)
    else:
        valid = (i - 1 for i in tree.meta if i - 1 < len(tree.children))
        return sum(sum_real(tree.children[k]) for k in valid)


def parse(data):
    n_children = data.pop()
    n_meta = data.pop()
    tree = Tree([], [])
    for _ in range(n_children):
        child, data = parse(data)
        tree.children.append(child)
    tree.meta.extend(data.pop() for _ in range(n_meta))
    return tree, data
