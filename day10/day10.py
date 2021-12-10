from math import floor

content = list(map(str, open("day10.txt").read().splitlines()))

scores = {")": [3, 1], "]": [57, 2], "}": [1197, 3], ">": [25137, 4]}
matched = {"(": ")", "[": "]", "{": "}", "<": ">"}

def check_syntax(line):

    closing = []
    for c in line:
        if c in matched.keys():
            closing.append(matched[c])
        if c in matched.values():
            if c == closing[-1]:
                closing.pop()
            else:
                return (scores[c][0], line, closing)
                
    return (0, line, closing)

def part1():
    running_total = 0
    for line in content:
        score, _, _ = check_syntax(line)
        running_total += score
    
    return running_total

def part2():
    corrupted = []
    for line in content:
        score, line, _ = check_syntax(line)
        if score > 0:
            corrupted.append(line)

    clean = [i for i in content if i not in corrupted]
    totals = []

    for line in clean:

        _, _, closing = check_syntax(line)

        running_total = 0
        closing.reverse()

        for c in closing:
            running_total = (running_total * 5) + scores[c][1]
        
        totals.append(running_total)
    
    totals.sort()
    return totals[floor(len(totals) / 2)]


print(f"Solution for part 1: {part1()}")
print(f"Solution for part 2: {part2()}")
