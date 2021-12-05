import math
import re
from collections import Counter
from typing import Tuple, List


class Vent:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def parse(line):
        regex = r"(\d+),(\d+) -> (\d+),(\d+)"
        match = re.match(regex, line)
        (x1, y1, x2, y2) = tuple(match.groups())
        return Vent(int(x1), int(y1), int(x2), int(y2))

    def get_orthogonal_trajectory(self) -> List[Tuple[int, int]]:
        if self.x1 == self.x2:
            y_coors = [self.y1, self.y2]
            return [(self.x1, y) for y in range(min(y_coors), max(y_coors) + 1)]

        if self.y1 == self.y2:
            x_coors = [self.x1, self.x2]
            return [(x, self.y1) for x in range(min(x_coors), max(x_coors) + 1)]

        return []

    def get_any_trajectory(self) -> List[Tuple[int, int]]:
        orthogonal = self.get_orthogonal_trajectory()
        if len(orthogonal) > 0:
            return orthogonal

        x_step = 1 if self.x1 < self.x2 else -1
        y_step = 1 if self.y1 < self.y2 else -1
        steps = abs(self.x1 - self.x2)

        return [(self.x1 + (s * x_step), self.y1 + (s * y_step)) for s in range(steps + 1)]


def part1():
    with open("input5.txt") as file:
        vents = [Vent.parse(line) for line in file.readlines()]

    points = Counter()
    for v in vents:
        trajectory = v.get_orthogonal_trajectory()
        points.update(trajectory)

    return sum([1 for p in points if points[p] > 1])


def part2():
    with open("input5.txt") as file:
        vents = [Vent.parse(line) for line in file.readlines()]

    points = Counter()
    for v in vents:
        trajectory = v.get_any_trajectory()
        points.update(trajectory)

    return sum([1 for p in points if points[p] > 1])


print(part1())
print(part2())
