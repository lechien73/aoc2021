content = [l.strip().split(" ") for l in open("day2.txt").readlines()]

directions = {"forward": 0, "up": 0, "down": 0}

for (d, v) in content:
    directions[d] += int(v)

print(directions["forward"] * (directions["down"] - directions["up"]))
