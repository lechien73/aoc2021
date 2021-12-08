content = [l.strip().split(" ") for l in open("day2.txt").readlines()]

directions = {"forward": 0, "depth": 0, "aim": 0}

for (d, v) in content:
    if d == "down":
        directions["aim"] += int(v)
    elif d == "up":
        directions["aim"] -= int(v)
    else:
        directions["forward"] += int(v)
        directions["depth"] += directions["aim"] * int(v)

print(directions["forward"] * directions["depth"])
