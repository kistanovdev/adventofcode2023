lines = [line.strip() for line in open("input.txt")]
total = 0


def mul(length):
    if length > 1:
        temp = 1
        for _ in range(length - 1):
            temp *= 2
        return temp

    return length


for line in lines:
    card, __input = line.split(":")
    winning, cards_input = __input.split("|")

    parsed_win = set([int(item) for item in winning.strip().split()])
    parsed_input = set([int(item) for item in cards_input.strip().split()])
    length = len(parsed_win & parsed_input)
    total += mul(length)


assert total == 23235
