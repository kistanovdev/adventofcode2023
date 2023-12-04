import sys

lines = [line.strip() for line in open('input_pt2.txt')]


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

    return tuple(sorted(res))


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

gears = []

for idx, row in enumerate(lines):
    for idx_j, char in enumerate(row):
        if char == "*":
            gears.append((idx, idx_j))


def get_possible_indexes(x, y):
    def get_above(x, y):
        if y == 0:
            return x, y
        return x, y - 1

    def get_below(x, y):
        if y == 139:
            return x, y
        return x, y + 1

    def get_left(x, y):
        if x == 0:
            return x, y
        return x - 1, y

    def get_right(x, y):
        if x == 139:
            return x,y
        return x + 1, y

    def get_up_left(x, y):
        if y == 0 or x == 0:
            return x, y
        return x - 1, y - 1

    def get_up_right(x, y):
        if y == 0 or x == 139:
            return x, y
        return x + 1, y - 1

    def get_down_left(x, y):
        if x == 139 or y == 0:
            return x, y
        return x - 1, y + 1

    def get_down_right(x, y):
        if x == 139 or y == 139:
            return x, y
        return x + 1, y + 1

    s = set()

    s.add(get_above(x, y))
    s.add(get_below(x, y))
    s.add(get_left(x, y))
    s.add(get_right(x, y))
    s.add(get_up_right(x, y))
    s.add(get_up_left(x, y))
    s.add(get_down_right(x, y))
    s.add(get_down_left(x, y))

    try:
        s.remove((x, y))
    except KeyError:
        pass

    return s


def do_search(digit_coordinates, x,y):

    for coordinate in digit_coordinates:
        for sub_index in coordinate:
            search_x, search_y = sub_index
            if search_x == x and search_y == y:
                return coordinate

    return -1

total = 0

def check_if_exists(a,b):

    def f(coordinate, lst):
        for item in lst:
            if coordinate == item:
                return True
        return False

    for result in search_results:
        for coordinate in result:
            if f(coordinate, b):
                return True


    return False

total = 0

def get_product(search_results):

    if len(search_results) == 1:
        return 0

    total = 1

    for res in search_results:
        number = read_digit(lines, res)
        total *= number
    return total

for gear in gears:
    x, y = gear
    possible_coordinates = get_possible_indexes(x, y)

    search_results = []
    for sub_x, sub_y in possible_coordinates:
        search_res = do_search(digit_coordinates, sub_x, sub_y)

        if search_res != -1:
            if not check_if_exists(search_results, search_res):
                search_results.append(search_res)
    product = get_product(search_results)
    total += product

print(total)


