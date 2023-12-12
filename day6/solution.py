lines = [line.strip() for line in open("input.txt")]
time = [int(x) for x in lines[0].split(":")[1].split()]
distance = [int(x) for x in lines[1].split(":")[1].split()]


# the formula is
# x is how much you're holding the button for
# button_held_for = (time - x)
# time_left_for_race = time - button_held_for
# speed = button_held_for
# distance_travelled = speed * time_left_for_race
def calculate(button_held_for, time, distance) -> bool:
    if button_held_for <= 0:
        return False
    if button_held_for >= time:
        return False

    time_left_for_race = time - button_held_for
    distance_travelled = button_held_for * time_left_for_race
    return distance_travelled >= distance

race_counter = []

for time, distance in zip(time, distance):

    count = 0
    for button_held_for in range(time):
        if calculate(button_held_for, time, distance):
            count += 1

    race_counter.append(count)

product = 1

for x in race_counter:
    product *= x

print(product)
assert product == 303600
