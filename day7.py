def part1():
    with open("input7.txt") as file:
        contents = file.read()
        crabs = [int(c) for c in contents.split(",")]
    # crabs = [16,1,2,0,4,2,7,1,2,14]

    max_position = max(crabs)
    position_costs = [(i, sum([abs(c-i) for c in crabs])) for i in range(max_position + 1)]
    sorted_costs = sorted(position_costs, key=lambda x: x[1])
    return sorted_costs[0]


def part2():
    with open("input7.txt") as file:
        contents = file.read()
        crabs = [int(c) for c in contents.split(",")]
    # crabs = [16,1,2,0,4,2,7,1,2,14]

    max_position = max(crabs)
    # Highly inefficient, the most inner formula was supposed to be something like n*n/2, but I was lazy :P
    position_costs = [(i, sum([sum([x for x in range(1, abs(c-i)+1)]) for c in crabs])) for i in range(max_position + 1)]
    sorted_costs = sorted(position_costs, key=lambda x: x[1])
    return sorted_costs[0]


print(part1())
print(part2())
