from statistics import median

ERROR_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}
PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}


def get_line_error(line):
    stack = []
    for c in line:
        if c in PAIRS.keys():
            stack.append(c)
        else:
            s = stack.pop()
            expected = PAIRS[s]
            if c != expected:
                return ERROR_POINTS[c]
    return 0


def complete_line(line):
    stack = []
    for c in line:
        if c in PAIRS.keys():
            stack.append(c)
        else:
            _s = stack.pop()

    score = 0
    while len(stack) > 0:
        s = stack.pop()
        score = (score*5) + COMPLETION_POINTS[PAIRS[s]]
    return score


def part1():
    with open("input10.txt") as file:
        return sum([get_line_error(line.strip()) for line in file.readlines()])


def part2():
    with open("input10.txt") as file:
        relevant = [line.strip() for line in file.readlines() if get_line_error(line.strip()) == 0]

    scores = [complete_line(line) for line in relevant]
    return median(scores)


print(part1())
print(part2())
