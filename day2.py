def part1():
    X_INC = "forward"
    Y_INC = "down"
    Y_DEC = "up"

    x = 0
    y = 0

    with open("input2.txt") as file:
        for line in file:
            (direction, step_str) = tuple(line.split())
            step = int(step_str)
            if direction == X_INC:
                x += step
            elif direction == Y_INC:
                y += step
            elif direction == Y_DEC:
                y -= step
            else:
                raise Exception(f"Unexpected direction {direction}")

    return x*y


def part2():
    AIM_INC = "down"
    AIM_DEC = "up"
    MOVE = "forward"

    aim = 0
    x = 0
    y = 0

    with open("input2.txt") as file:
        for line in file:
            (direction, step_str) = tuple(line.split())
            step = int(step_str)
            if direction == AIM_INC:
                aim += step
            elif direction == AIM_DEC:
                aim -= step
            elif direction == MOVE:
                x += step
                y += aim*step
            else:
                raise Exception(f"Unexpected direction {direction}")

    return x*y


print(part1())
print(part2())
