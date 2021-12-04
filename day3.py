def most_frequent(elements):
    if len([e for e in elements if e == 1]) == len([e for e in elements if e == 0]):
        return 1
    return max(set(elements), key=elements.count)


def least_frequent(elements):
    if len([e for e in elements if e == 1]) == len([e for e in elements if e == 0]):
        return 0
    return min(set(elements), key=elements.count)


def get_numbers_rating(matrix, selecting_fun):
    columns_count = len(matrix[0])
    rows_count = len(matrix)
    relevant_indices = set(range(rows_count))

    for i in range(columns_count):
        relevant_elements = [matrix[j][i] for j in relevant_indices]
        leading_element = selecting_fun(relevant_elements)
        subtract_indices = [j for j in range(rows_count) if matrix[j][i] != leading_element]
        relevant_indices -= set(subtract_indices)
        if len(relevant_indices) == 1:
            break

    return "".join([str(x) for x in matrix[relevant_indices.pop()]])


def part1():
    with open("input3.txt") as file:
        rows = [[int(x) for x in line.strip()] for line in file.readlines()]

    columns = [[row[i] for row in rows] for i in range(len(rows[0]))]
    gamma_rates = [str(most_frequent(column)) for column in columns]
    epsilon_rates = ["0" if g == "1" else "1" for g in gamma_rates]

    gamma_rates_str = "".join(gamma_rates)
    epsilon_rates_str = "".join(epsilon_rates)

    return int(gamma_rates_str, 2) * int(epsilon_rates_str, 2)


def part2():
    with open("input3.txt") as file:
        matrix = [[int(x) for x in line.strip()] for line in file.readlines()]

    oxygen_rating_str = get_numbers_rating(matrix, most_frequent)
    co2_rating_str = get_numbers_rating(matrix, least_frequent)

    print(int(oxygen_rating_str, 2))
    print(int(co2_rating_str, 2))

    return int(oxygen_rating_str, 2) * int(co2_rating_str, 2)


# print(part1())
print(part2())
