content = [i.strip() for i in open("day8.txt").readlines()]

# Following the theme - part 1...not too bad

def part1():
    count = 0

    for c in content:
        outputs = c.split(" | ")[1].split(" ")
        for o in outputs:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                count += 1

    return count

# Part 2 - Abandon Hope All Ye Who Enter Here

def find3(inputs, num_set):
    for i in inputs:
        if len(i) == 5 and all(n in i for n in num_set[1]):
            num_set[3] = i

def find9(inputs, num_set):
    for i in inputs:
        num_set[9] = "".join(list(set(num_set[3] + num_set[4])))

def find0(inputs, num_set):
    for i in inputs:
        if len(i) == 6 and all(n in i for n in num_set[1]) and not all(n in i for n in num_set[9]):
            num_set[0] = i

def find6(inputs, num_set):
    for i in inputs:
        if len(i) == 6 and not all(n in i for n in num_set[0]) and not all(n in i for n in num_set[9]):
            num_set[6] = i

def find5(inputs, num_set):
    for i in inputs:
        if len(i) == 5 and not all(n in i for n in num_set[3]) and all(n in i for n in list(set(num_set[4]) - set(num_set[1]))):
            num_set[5] = i

def find2(inputs, num_set):
    for i in inputs:
        if len(i) == 5 and not all(n in i for n in num_set[9]) and all(n in i for n in list(set(num_set[8]) - set(num_set[5]))):
            num_set[2] = i

def part2():
    total = 0

    for c in content:

        inputs = c.split(" | ")[0].split(" ")
        outputs = c.split(" | ")[1].split(" ")
        
        for num in range(len(inputs)):

            num_set = {1: "".join([i for i in inputs if len(i) == 2]), 
                    2: "", 
                    3: "",
                    4: "".join([i for i in inputs if len(i) == 4]), 
                    5: "", 
                    6: "", 
                    7: "".join([i for i in inputs if len(i) == 3]), 
                    8: "".join([i for i in inputs if len(i) == 7]), 
                    9: "", 
                    0: ""}

            find3(inputs, num_set)
            find9(inputs, num_set)
            find0(inputs, num_set)
            find6(inputs, num_set)
            find5(inputs, num_set)
            find2(inputs, num_set)

        display = ""

        for o in outputs:            
            for k, v in num_set.items():
                if set(o) == set(v):
                    display += str(k)

        total += int(display)
    
    return total

print(f"Solution to part 1 {part1()}")
print(f"Solution to part 2: {part2()}")
