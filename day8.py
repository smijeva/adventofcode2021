# 1, 4, 7, 8 digits
UNIQUE_SEGMENTS = [2, 4, 3, 7]


def part1():
    with open("input8.txt") as file:
        outputs = [line.split('|')[1] for line in file.readlines()]

    return sum([len([True for number in o.split() if len(number) in UNIQUE_SEGMENTS]) for o in outputs])


def get_output(line):
    inp, output = line.split("|")
    digits = [set(x) for x in inp.split()]

    one = [x for x in digits if len(x) == 2][0]
    four = [x for x in digits if len(x) == 4][0]
    seven = [x for x in digits if len(x) == 3][0]
    eight = [x for x in digits if len(x) == 7][0]

    a_seg = (seven - one).pop()
    three = [x for x in digits if len(x) == 5 and len(x.intersection(one)) == 2][0]
    nine = [x for x in digits if len(x) == 6 and len(x.intersection(four)) == 4][0]
    e_seg = (eight - nine).pop()
    two = [x for x in digits if len(x) == 5 and e_seg in x][0]
    f_seg = (three - two).pop()
    c_seg = (one - set(f_seg)).pop()
    six = [x for x in digits if len(x) == 6 and c_seg not in x][0]
    zero = [x for x in digits if len(x) == 6 and c_seg in x and e_seg in x][0]
    d_seg = (eight - zero).pop()
    five = [x for x in digits if len(x) == 5 and c_seg not in x and e_seg not in x][0]
    e_seg = (eight - five - one).pop()
    b_seg = (eight - three - two).pop()

    output_sum = 0
    for j, o in enumerate([set(x) for x in output.split()]):
        i = 3 - j
        if o == zero:
            output_sum += 0 * (10 ** i)
        elif o == one:
            output_sum += 1 * (10 ** i)
        elif o == two:
            output_sum += 2 * (10 ** i)
        elif o == three:
            output_sum += 3 * (10 ** i)
        elif o == four:
            output_sum += 4 * (10 ** i)
        elif o == five:
            output_sum += 5 * (10 ** i)
        elif o == six:
            output_sum += 6 * (10 ** i)
        elif o == seven:
            output_sum += 7 * (10 ** i)
        elif o == eight:
            output_sum += 8 * (10 ** i)
        elif o == nine:
            output_sum += 9 * (10 ** i)
        else:
            raise Exception(f"Unknown output {o}")
    return output_sum


def part2():
    with open("input8.txt") as file:
        return sum([get_output(line) for line in file.readlines()])


print(part1())
print(part2())
