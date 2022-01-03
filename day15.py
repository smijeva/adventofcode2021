def part1():
    with open("input15.txt") as file:
        matrix = [[int(c) for c in line if c != '\n'] for line in file.readlines()]

    prices = [[(-1, -1, "X") for _i in row] for row in matrix]

    prices[0][0] = (0, matrix[0][0], "X")
    for i in range(1, len(matrix)):
        prices[i][0] = (prices[i-1][0][0] + matrix[i][0], matrix[i][0], "U")
    for j in range(1, len(matrix[0])):
        prices[0][j] = (prices[0][j-1][0] + matrix[0][j], matrix[0][j], "L")

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            up = prices[i-1][j][0]
            left = prices[i][j-1][0]
            if up < left:
                p = up + matrix[i][j]
                prices[i][j] = (p, matrix[i][j], "U")
            else:
                p = left + matrix[i][j]
                prices[i][j] = (p, matrix[i][j], "L")

    for row in prices:
        print(row)
    return prices[-1][-1]


print(part1())
