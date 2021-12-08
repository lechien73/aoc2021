content = [int(l) for l in open("day1.txt").readlines()]

def solve(input_array):

    return sum(input_array[i] > input_array[i-1] for i in range(1, len(input_array)))

print(f"Part 1: {solve(content)}")
print(f"Part 2: {solve([sum(content[i:i+3]) for i in range(len(content) - 2)])}")
