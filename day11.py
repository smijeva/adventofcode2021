def get_neighbours(matrix, coors):
    x, y = coors
    x_max = len(matrix)
    y_max = len(matrix[0])
    all_neighs = [(x + x_s, y + y_s) for x_s in range(-1, 2) for y_s in range(-1, 2) if x + x_s != x or y + y_s != y]
    return [(x, y) for x, y in all_neighs if -1 < x < x_max and -1 < y < y_max]


def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def step(matrix):
    new_matrix = [[val+1 if val < 9 else 0 for val in line] for line in matrix]

    flashes_queue = [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if new_matrix[x][y] == 0]
    all_flashes = set(flashes_queue)

    while len(flashes_queue) > 0:
        f = flashes_queue.pop()
        neighbours = get_neighbours(new_matrix, f)
        for n in neighbours:
            x, y = n
            val = new_matrix[x][y]
            if val == 0:
                # already flashed
                continue
            new_matrix[x][y] = val + 1 if val < 9 else 0
            if new_matrix[x][y] == 0 and n not in all_flashes:
                flashes_queue.append(n)
                all_flashes.add(n)

    return new_matrix, len(all_flashes)


def part1():
    with open('input11.txt') as file:
        matrix = [[int(c) for c in line.strip()] for line in file]

    flashes = 0
    for i in range(100):
        matrix, f = step(matrix)
        flashes += f
    return flashes


def part2():
    with open('input11.txt') as file:
        matrix = [[int(c) for c in line.strip()] for line in file]

    i = 1
    while True:
        matrix, _f = step(matrix)
        if all(all(val == 0 for val in row) for row in matrix):
            return i
        i += 1


print(part1())
print(part2())
