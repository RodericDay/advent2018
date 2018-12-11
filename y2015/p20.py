def main(text, simple):
    N = 1000000
    goal = int(text)
    houses = [0 for n in range(N)]
    for elf in range(1, N):
        for count, visit in enumerate(range(elf, N, elf)):
            if simple:
                houses[visit] += elf * 10
            elif count < 50:
                houses[visit] += elf * 11
            else:
                break
            if houses[visit] > goal:
                print(visit)
                return
