def part1():
    with open("input1.txt") as file:
        measurements = [int(line) for line in file]

    previous = measurements[:-1]
    current = measurements[1:]
    increases = [True for (p, c) in zip(previous, current) if p < c]

    return len(increases)


def part2():
    with open("input1.txt") as file:
        measurements = [int(line) for line in file]

    three_measurements = [sum(measurements[i:i+3]) for i in range(len(measurements) - 2)]

    previous = three_measurements[:-1]
    current = three_measurements[1:]

    increases = [True for (p, c) in zip(previous, current) if p < c]

    return len(increases)


print(part1())
print(part2())
