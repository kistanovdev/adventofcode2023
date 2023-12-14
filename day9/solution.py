from copy import copy

with open("input.txt") as file:
    reports = [[int(x) for x in line.split()] for line in file]


def reduce(report):
    buff = []

    for idx in range(len(report) - 1):
        buff.append(report[idx + 1] - report[idx])

    return buff


def all_zeros(report: list[int]) -> bool:
    return all([x == 0 for x in report])


def get_all_reductions(report: list[int]) -> list[list[int]]:
    result = []

    copy_report = report

    while not all_zeros(copy_report):
        result.append(copy_report)
        copy_report = reduce(copy_report)

    result.append(copy_report)
    return result


def extrapolate_final_number(reductions: list[list[int]]) -> int:
    temp_reduction = copy(reductions)
    temp_reduction.reverse()

    for idx in range(len(temp_reduction) - 1):
        num1 = temp_reduction[idx][-1]
        num2 = temp_reduction[idx + 1][-1]
        temp_reduction[idx + 1].append(num1 + num2)

    return temp_reduction[-1][-1]


def extrapolate_final_number_pt2(reductions: list[list[int]]) -> int:
    temp_reduction = copy(reductions)
    temp_reduction.reverse()

    for idx in range(len(temp_reduction) - 1):
        num1 = temp_reduction[idx][0]
        num2 = temp_reduction[idx + 1][0]
        temp_reduction[idx + 1].insert(0, num2 - num1)

    return temp_reduction[-1][0]


original_reports = copy(reports)
total = 0
for report in reports:
    reduction_reports = get_all_reductions(report)
    res = extrapolate_final_number(reduction_reports)
    total += res

assert original_reports == reports
print(total)
assert total == 1898776583
total = 0
for report in reports:
    reduction_reports = get_all_reductions(report)
    res = extrapolate_final_number_pt2(reduction_reports)
    total += res

assert original_reports == reports
print(total)
assert total == 1100
