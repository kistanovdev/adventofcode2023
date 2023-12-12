if __name__ == "__main__":
    find_first_digit = lambda lst: next((x for x in lst if x.isdigit()), None)
    find_last_digit = lambda lst: next((x for x in reversed(lst) if x.isdigit()), None)
    sum_first_last = lambda x: int(find_first_digit(x) + find_last_digit(x))
    print(sum([sum_first_last(line.strip()) for line in open("input.txt")]))
