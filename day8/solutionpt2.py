import re
from math import gcd

steps = "".join([line.strip() for line in open("steps.txt")])

steps = [x for x in steps]

move_lookup = {}

with open("mapping.txt") as f:
    for line in f.readlines():
        pattern = re.compile("[A-z]{3}")
        x, y, z = pattern.findall(line)
        move_lookup[x] = (y, z)

paths = []
for k in move_lookup.keys():
    if k[-1] == "A":
        paths.append(k)


def check_all(paths):
    return all([x[-1] == "Z" for x in paths])


counts = []
for path in paths:
    curr = path
    count = 0
    while curr[-1] != "Z":
        for step in steps:
            count += 1

            L, R = move_lookup[curr]
            if step == "L":
                curr = L
            else:
                curr = R

            if curr[-1] == "Z":
                break

    counts.append(count)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_array(arr):
    lcm_value = arr[0]
    for i in range(1, len(arr)):
        lcm_value = lcm(lcm_value, arr[i])
    return lcm_value


assert lcm_array(counts) == 21165830176709
