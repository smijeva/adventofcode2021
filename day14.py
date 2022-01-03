from collections import Counter
from datetime import datetime
from typing import Dict


def parse_inputs():
    with open("input14.txt") as file:
        polymers = file.readline().strip()
        file.readline()
        rules = {}
        for line in file.readlines():
            left, right = line.strip().split(' -> ')
            rules[left] = right

    return polymers, rules


def expand(polymers: str, rules: Dict[str, str], depth: int) -> Counter:
    counter = Counter(polymers[0])

    for i in range(len(polymers) - 1):
        print(polymers[i:i + 2], datetime.now())
        stack = [("", -1) for _i in range((2*depth)+1)]
        stack[0] = (polymers[i:i + 2], 0)
        pointer = 0

        while True:
            r, d = stack[pointer]
            if d == -1:
                break

            if d == depth:
                counter.update(r[1])
                stack[pointer] = ("", -1)
                pointer -= 1
                continue

            rule = rules.get(r)
            if rule is None:
                counter.update(r[1])
                stack[pointer] = ("", -1)
                pointer -= 1
                continue

            stack[pointer] = (r[0] + rule, d+1)
            pointer += 1
            stack[pointer] = (rule + r[1], d+1)

    print(counter)
    return counter


def get_result(c: Counter) -> int:
    return c.most_common()[0][1] - c.most_common()[-1][1]


polymers, rules = parse_inputs()
# print(expand(polymers, rules, 1, 0))
# print(expand(polymers, rules, 2, 0))
# print(expand(polymers, rules, 3, 0))
# print(get_result(expand(polymers, rules, 10)))
print(get_result(expand(polymers, rules, 40)))
