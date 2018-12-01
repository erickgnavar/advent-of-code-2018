from collections import Counter
from itertools import cycle


def calculate(input_):
    """
    Given a string with numbers separated by comma like "+1, -2"
    calculate the sum of the numbers
    """
    return sum([int(x.strip()) for x in input_.split(",") if x])


def find_reached_twice(input_):
    """
    Given a string with numbers separated by comma like "+1, -2"
    calculate the frequency reached twice
    """
    counter = Counter()
    values = cycle([int(x.strip()) for x in input_.split(",") if x])
    frequency = 0
    counter[frequency] += 1
    for value in values:
        frequency += value
        counter[frequency] += 1
        if counter[frequency] == 2:
            break
    return frequency


def run():
    with open("../inputs/day01.txt") as f:
        raw = f.read().replace("\n", ",")
        print(f"The reached frequency is {calculate(raw)}")
        print(f"The first frequency reached twice is {find_reached_twice(raw)}")
