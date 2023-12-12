lines = [line.strip() for line in open("input.txt")]
total = 0


def mul(length):
    if length > 1:
        temp = 1
        for _ in range(length - 1):
            temp *= 2
        return temp

    return length


def add_up(cur_idx, length, mem):
    add_amount = mem[cur_idx]

    if cur_idx + 1 + length > len(mem):
        end = len(mem)
    else:
        end = cur_idx + 1 + length

    for idx in range(cur_idx + 1, end):
        mem[idx] += add_amount


mem_lookup = [1 for _ in range(len(lines))]

for idx, line in enumerate(lines):
    card, __input = line.split(":")
    winning, cards_input = __input.split("|")

    parsed_win = set([int(item) for item in winning.strip().split()])
    parsed_input = set([int(item) for item in cards_input.strip().split()])

    match = len(parsed_win & parsed_input)
    add_up(idx, match, mem_lookup)


print(sum(mem_lookup))
