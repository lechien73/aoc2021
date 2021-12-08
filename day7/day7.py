from math import floor
import statistics

content = list(map(int, open("day7.txt").read().split(",")))

def part1():

    target = statistics.median(content)

    fuel = sum([abs(c - target) for c in content])

    return fuel

def part2():

    target = floor(statistics.mean(content))
    content.sort()

    fuel = 0

    for c in content:
        moves = max(c, target) - min(c, target)
        for i in range(1, moves + 1):
            fuel += i

    return fuel

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")