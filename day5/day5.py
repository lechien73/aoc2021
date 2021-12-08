from collections import Counter

content = [l.strip().split(" -> ") for l in open("day5.txt").readlines()]


def part1():

    vents = Counter()
    for c in content:
        x1, y1 = map(int, c[0].split(","))
        x2, y2 = map(int, c[1].split(","))
        if x1 == x2:
            vents.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            vents.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
    return sum(count > 1 for count in vents.values())

def part2():
    
    vents = Counter()
    for c in content:
        x1, y1 = map(int, c[0].split(","))
        x2, y2 = map(int, c[1].split(","))
        if x1 == x2:
            vents.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            vents.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
        elif abs(x2 - x1) == abs(y2 - y1):
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            vents.update((x1 + i * dx, y1 + i * dy) for i in range(abs(x2 - x1) + 1))
    return sum(count > 1 for count in vents.values())


print(f"Solution to Part 1: {part1()}")
print(f"Solution to Part 2: {part2()}")
