print(
    sum(
        int(next((x for x in line if x.isdigit()), "0"))
        + int(next((x for x in reversed(line) if x.isdigit()), "0"))
        for line in open("input.txt").read().splitlines()
    )
)
