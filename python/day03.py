import re


def _parse_line(line):
    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    match = regex.match(line)
    if match:
        return match.groups()
    else:
        return None


def run():
    matrix = [
        [0 for i in range(1000)] for x in range(1000)
    ]
    with open("../inputs/day03.txt") as f:
        lines = f.readlines()

        for line in lines:
            if not line:
                continue
            result = _parse_line(line)
            if result:
                id_, left, top, width, height = result
                left = int(left)
                top = int(top)
                width = int(width)
                height = int(height)
                for x in range(left, left + width):
                    for y in range(1000 - (top + height), 1000 - top):
                        matrix[x][y] += 1
        counter = 0
        for i in range(1000):
            for j in range(1000):
                if matrix[i][j] >= 2:
                    counter += 1
        # Part 1
        print(f"Inches overlaped: {counter}")

        result_id = None
        for line in lines:
            if not line:
                continue
            result = _parse_line(line)
            if result:
                id_, left, top, width, height = result
                left = int(left)
                top = int(top)
                width = int(width)
                height = int(height)
                flag = True
                for x in range(left, left + width):
                    for y in range(1000 - (top + height), 1000 - top):
                        flag = flag and matrix[x][y] == 1
                if flag:
                    result_id = id_

        # part 2
        print(f"Box id with no overlap: #{result_id}")
