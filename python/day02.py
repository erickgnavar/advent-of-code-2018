from collections import Counter
from itertools import product


def count_letters(input_):
    """
    Given an input_ like "abcdef" return a tuple with the result of the following rules
    a letter appears exactly 2 times
    a letter appears exactly 3 times
    """
    counter = Counter(input_)
    two_times = 0
    three_times = 0
    for quantity in counter.values():
        if quantity == 2:
            two_times += 1
        elif quantity == 3:
            three_times += 1
    return two_times > 0, three_times > 0


def check_repeated(str1, str2):
    """
    Given 2 string check if these strings have a diff of 1 character
    if it's the case return the position of the character otherwise return None
    """
    assert len(str1) == len(str2)
    position = None
    quantity = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            quantity += 1
            position = i
    if quantity == 1:
        return position
    else:
        return None


def run():
    with open("../inputs/day02.txt") as f:
        lines = f.readlines()

        two_times, three_times = 0, 0
        for line in lines:
            if not line:
                continue
            two, three = count_letters(line)
            if two:
                two_times += 1
            if three:
                three_times += 1
        print(f"The checksum is {two_times * three_times}")

        for id_1, id_2 in product(lines, lines):
            if id_1 == id_2:
                continue
            pos = check_repeated(id_1, id_2)
            if pos is not None:
                res = id_1[0:pos] + id_1[pos + 1:]
                print(f"The result is {res}")
