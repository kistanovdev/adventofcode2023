import re

steps = "".join([line.strip() for line in open("steps.txt")])

steps = [x for x in steps]

move_lookup = {}

with open("mapping.txt") as f:
    for line in f.readlines():
        pattern = re.compile("[A-z]{3}")
        x, y, z = pattern.findall(line)
        move_lookup[x] = (y, z)

curr = "AAA"
count = 0
while curr != "ZZZ":
    for step in steps:
        count += 1
        L, R = move_lookup[curr]
        if step == "L":
            curr = L
        else:
            curr = R
        if curr == "ZZZ":
            break

assert count == 21409
