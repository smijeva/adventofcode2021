def pretty_print(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])
    print("-" * 40)


def flip_horizontally(matrix):
    return [[matrix[y][-x] for x in range(len(matrix[0]))] for y in range(len(matrix))]


def flip_vertically(matrix):
    return [[matrix[-y][x] for x in range(len(matrix[0]))] for y in range(len(matrix))]


def fold(matrix, axis, n):
    n_x = len(matrix[0])
    n_y = len(matrix)

    if axis == "y":
        if n < n_y // 2:
            matrix = flip_vertically(matrix)
        new_matrix = [["#" if matrix[y][x] == "#" else "." for x in range(n_x)] for y in range(n)]
        for y in range(n + 1, n_y):
            for x in range(n_x):
                if matrix[y][x] == "#":
                    n_dist = y - n
                    new_matrix[n - n_dist][x] = "#"
        return new_matrix
    else:
        if n < n_x // 2:
            matrix = flip_horizontally(matrix)
        new_matrix = [["#" if matrix[y][x] == "#" else "." for x in range(n)] for y in range(n_y)]
        for y in range(n_y):
            for x in range(n+1, n_x):
                if matrix[y][x] == "#":
                    n_dist = x - n
                    new_matrix[y][n - n_dist] = "#"
        return new_matrix


def part1():
    with open("input13.txt") as file:
        dots = []
        instructions = []
        for l in file.readlines():
            if l.isspace():
                continue
            elif l.startswith("fold"):
                parts = l.strip().split("=")
                axis = parts[0][-1]
                n = int(parts[1])
                instructions.append((axis, n))
            else:
                x, y = [int(i) for i in l.strip().split(",")]
                dots.append((x, y))

    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)

    print(max_x)
    print(max_y)

    matrix = [['.' for _j in range(max_x + 1)] for _i in range(max_y + 1)]
    for x, y in dots:
        matrix[y][x] = '#'
    m = fold(matrix, instructions[0][0], instructions[0][1])

    return sum([sum([1 for ele in row if ele == '#']) for row in m])

    # for i in instructions:
    #     matrix = fold(matrix, i[0], i[1])
    #
    # pretty_print(matrix)
    # return 0


def part2():
    with open("input13.txt") as file:
        dots = []
        instructions = []
        for l in file.readlines():
            if l.isspace():
                continue
            elif l.startswith("fold"):
                parts = l.strip().split("=")
                axis = parts[0][-1]
                n = int(parts[1])
                instructions.append((axis, n))
            else:
                x, y = [int(i) for i in l.strip().split(",")]
                dots.append((x, y))

    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)

    print(max_x)
    print(max_y)

    matrix = [['.' for _j in range(max_x + 1)] for _i in range(max_y + 1)]
    for x, y in dots:
        matrix[y][x] = '#'

    for i in instructions:
        matrix = fold(matrix, i[0], i[1])

    pretty_print(matrix)
    return 0


print(part1())
part2()
