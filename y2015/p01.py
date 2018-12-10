def main(text, simple):
    if simple:
        print(text.count('(') - text.count(')'))

    else:
        height = 0
        for i, c in enumerate(text, 1):
            height += 1 if c == '(' else -1
            if height == -1:
                print(i)
                break
