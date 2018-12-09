def main(text, simple):
    n = int(text)
    i = 0
    if simple:
        track = [0]
        for _ in range(2017):
            i = (i + n) % len(track) + 1
            track.insert(i, len(track))
        print(track[i + 1])
    else:
        for x in range(5 * 10**7):
            i = (i + n) % (x + 1) + 1
            if i == 1:
                ans = x
        print(ans)
