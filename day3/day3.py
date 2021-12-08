from copy import deepcopy

content = [i.strip() for i in open("day3.txt").readlines()]


def make_counts(data):
    count_dict = {c: {0: 0, 1: 0} for c in range(len(data[0]))}

    for c in data:
        for i in range(len(c)):
            count_dict[i][int(c[i])] += 1

    return count_dict


def keep_number(pos, num, numbers):
    return [c for c in numbers if int(c[pos]) == num]


def part1():

    gamma = "".join(map(str, [max(v, key=v.get) for v in counts.values()]))
    epsilon = "".join(map(str, [int(not int(g)) for g in gamma]))

    return int(gamma, 2) * int(epsilon, 2)


def part2():

    nums = content.copy()
    _counts = deepcopy(counts)
    for k in _counts:
        num = 1 if _counts[k][1] >= _counts[k][0] else 0
        nums = keep_number(k, num, nums)
        _counts = make_counts(nums)
        if len(nums) == 1:
            break

    nums2 = content.copy()
    for k in _counts:
        nums2 = keep_number(k, min(_counts[k], key=_counts[k].get), nums2)
        _counts = make_counts(nums2)
        if len(nums2) == 1:
            break

    return int(nums[0], 2) * int(nums2[0], 2)


counts = make_counts(content)
print(f"Solution to Part 1: {part1()}")
print(f"Solution to Part 2: {part2()}")
