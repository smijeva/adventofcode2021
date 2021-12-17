import math


def get_neighbours(matrix, coors):
    x, y = coors
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if x < (len(matrix) - 1):
        neighbours.append((x + 1, y))
    if y < (len(matrix[0]) - 1):
        neighbours.append((x, y + 1))
    return neighbours


def risk_level(matrix, coors):
    neighbours = get_neighbours(matrix, coors)
    x, y = coors

    if all([matrix[n0][n1] > matrix[x][y] for n0, n1 in neighbours]):
        return matrix[x][y] + 1
    return 0


def is_low(matrix, coors):
    return risk_level(matrix, coors) > 0


def get_lows(matrix):
    return [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if is_low(matrix, (x, y))]


def get_level(matrix, coors):
    return matrix[coors[0]][coors[1]]


def get_basin(matrix, coors):
    basin = [coors]
    queue = get_neighbours(matrix, coors)

    while len(queue) > 0:
        candidate = queue.pop()
        if candidate in basin or get_level(matrix, candidate) == 9:
            continue

        can_neighbours = get_neighbours(matrix, candidate)
        if any([True for n in can_neighbours if n in basin and get_level(matrix, n) < get_level(matrix, candidate)]):
            basin.append(candidate)
            queue += can_neighbours

    return basin


def part1():
    with open("input9.txt") as file:
        matrix = [[int(i) for i in line.strip()] for line in file.readlines()]

    return sum([risk_level(matrix, (x, y)) for x in range(len(matrix)) for y in range(len(matrix[0]))])


def part2():
    with open("input9.txt") as file:
        matrix = [[int(i) for i in line.strip()] for line in file.readlines()]

    basin_sizes = sorted([len(get_basin(matrix, seed)) for seed in get_lows(matrix)], reverse=True)
    return math.prod(basin_sizes[:3])


print(part1())
print(part2())
