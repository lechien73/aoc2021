content = [list(map(int, i.strip())) for i in open("day9.txt").readlines()]

low_points = []
done = {}


def check_neighbours(y, x):

    checks = {"n": True, "s": True, "e": True, "w": True}
    if x == 0:
        checks["w"] = False
    if y == 0:
        checks["n"] = False
    if x == len(content[c]) - 1:
        checks["e"] = False
    if y == len(content) - 1:
        checks["s"] = False

    return checks


def check(d, checks, c, loc):

    if d == "n":
        return True if not checks["n"] or content[c][loc] < content[c-1][loc] else False
    if d == "s":
        return True if not checks["s"] or content[c][loc] < content[c+1][loc] else False
    if d == "e":
        return True if not checks["e"] or content[c][loc] < content[c][loc+1] else False
    if d == "w":
        return True if not checks["w"] or content[c][loc] < content[c][loc-1] else False

    return False


for c in range(len(content)):
    for loc in range(len(content[c])):

        checks = check_neighbours(c, loc)
        if check("n", checks, c, loc) and check("s", checks, c, loc) and check("e", checks, c, loc) and check("w", checks, c, loc):
            low_points.append((c, loc))


def get_neighbours(row, col):
    result = []
    for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = (row + n[0], col + n[1])
        if y < 0 or x < 0 or y > 99 or x > 99:
            continue
        result.append((y, x))
    return result


def build_basin(y, x):
    points = [(y, x)]
    done[(y, x)] = 1

    for row, col in get_neighbours(y, x):
        if (row, col) in done or content[row][col] >= 9:
            continue
        points += build_basin(row, col)

    return points


def part1():
    risk = 0
    for y, x in low_points:
        risk += content[y][x] + 1
    return risk


def part2():
    basins = []
    for y, x in low_points:
        basins.append(set(build_basin(y, x)))
    sizes = sorted([len(b) for b in basins], reverse=True)
    total = sizes[0] * sizes[1] * sizes[2]
    return total


print(f"Solution for part 1: {part1()}")
print(f"Solution for part 2: {part2()}")
