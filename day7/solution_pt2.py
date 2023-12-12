from functools import cmp_to_key

deck = [line.strip().split() for line in open("input.txt")]
for line in deck:
    line[1] = int(line[1])

value_lookup = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def custom_eval(deck):
    char_counts = {}

    for char in deck:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    if len(char_counts) == 1:
        return 0  # AAAAA

    if len(char_counts) == 2:
        if "J" in char_counts.keys():
            return 0  # can pretend to be 5 of kind

        if 4 in char_counts.values():
            return 1  # FOUR OF A KIND
        if 3 in char_counts.values() and 2 in char_counts.values():
            return 2  # FULL HOUSE

    if "J" in char_counts.keys():
        saved_val = char_counts["J"]
        del char_counts["J"]
        max_key = max(char_counts, key=char_counts.get)
        char_counts[max_key] += saved_val
        if 4 in char_counts.values():
            return 1  # FOUR OF A KIND
        if 3 in char_counts.values() and 2 in char_counts.values():
            return 2  # FULL HOUSE
    else:
        print("did not find a J")

    if 3 in char_counts.values():
        return 3  # three of a kind

    if list(char_counts.values()).count(2) == 2:
        return 4  # two pair
    if list(char_counts.values()).count(2) == 1:
        return 5  # 1 pair
    assert len(char_counts.values()) == 5
    return 6  # everything else


def custom_cmp(value_a, value_b):
    a, _ = value_a
    b, _ = value_b
    val_a = custom_eval(a)
    val_b = custom_eval(b)

    if val_a == val_b:
        for x, y in zip(a, b):
            if value_lookup[x] != value_lookup[y]:
                if value_lookup[x] > value_lookup[y]:
                    return -1
                else:
                    return 1
        return 0

        return True

    if val_a > val_b:
        return 1
    else:
        return -1


my_custom_cmp = cmp_to_key(custom_cmp)

deck.sort(key=my_custom_cmp)
deck.reverse()

total = 0
for idx, card in enumerate(deck):
    _, number = card
    total += (idx + 1) * number

print(total)
assert total == 249631254
