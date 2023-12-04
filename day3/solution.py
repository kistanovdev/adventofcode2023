import sys

lines = [line.strip() for line in open('input.txt')]


def extract_number_coordinates(row_idx, line):
    buff = []
    res = []
    for idx, item in enumerate(line):
        if item.isdigit():
            buff.append((row_idx, idx))
        else:
            if buff:
                res.append(buff)
                buff = []
    if buff:
        res.append(buff)

    return res


def above(matrix, x, y) -> bool:
    if y == 0:
        return False
    return check_symbol(matrix, x, y - 1)


def below(matrix, x, y) -> bool:
    if y == 139:
        return False
    return check_symbol(matrix, x, y + 1)


def left(matrix, x, y) -> bool:
    if x == 0:
        return False
    return check_symbol(matrix, x - 1, y)


def right(matrix, x, y) -> bool:
    if x == 139:
        return False
    return check_symbol(matrix, x + 1, y)


def diagonally_up_left(matrix, x, y) -> bool:
    if x == 0:
        return False
    if y == 0:
        return False
    return check_symbol(matrix, x - 1, y - 1)


def diagonally_down_left(matrix, x, y) -> bool:
    if y == 139:
        return False
    if x == 0:
        return False
    return check_symbol(matrix, x - 1, y + 1)


def diagonally_up_right(matrix, x, y) -> bool:
    if y == 0:
        return False
    if x == 139:
        return False
    return check_symbol(matrix, x + 1, y - 1)


def diagonally_down_right(matrix, x, y) -> bool:
    if x == 139:
        return False
    if y == 139:
        return False
    return check_symbol(matrix, x + 1, y + 1)


def check_symbol(matrix, x, y) -> bool:
    if matrix[x][y] == "." or matrix[x][y].isdigit():
        return False

    assert matrix[x][y] in "#$%&*+-/=@"
    return True


def check_coordinate(matrix, coordinate) -> bool:
    x, y = coordinate

    assert matrix[x][y] in "0123456789"
    bools = []

    bools.append(right(matrix, x, y))
    bools.append(left(matrix, x, y))
    bools.append(above(matrix, x, y))
    bools.append(below(matrix, x, y))
    bools.append(diagonally_down_right(matrix, x, y))
    bools.append(diagonally_down_left(matrix, x, y))
    bools.append(diagonally_up_left(matrix, x, y))
    bools.append(diagonally_up_right(matrix, x, y))

    # if any(bools):
    #     print(f"DEBUG x {x} y {y}")
    #     print(bools)

    return any(bools)


digit_coordinates = []


def read_digit(matrix, coordinates):
    buff = []
    for x, y in coordinates:
        buff.append(matrix[x][y])

    return int(''.join(buff))


for idx, row in enumerate(lines):
    digit_coordinates.extend(extract_number_coordinates(idx, row))

total = 0
alone = []
for coordinate in digit_coordinates:

    number = read_digit(lines, coordinate)

    if number == 484:
        print("let's debug this bitch")

    bool_buff = []
    for x, y in coordinate:
        bool_buff.append(check_coordinate(lines, (x, y)))


    if any(bool_buff):
        total += number
    else:
        alone.append(number)

print(total)
print(alone)
