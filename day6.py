from typing import List

AGES = [1, 1, 3, 5, 3, 1, 1, 4, 1, 1, 5, 2, 4, 3, 1, 1, 3, 1, 1, 5, 5, 1, 3, 2, 5, 4, 1, 1, 5, 1, 4, 2, 1, 4, 2, 1, 4,
        4, 1, 5, 1, 4, 4, 1, 1, 5, 1, 5, 1, 5, 1, 1, 1, 5, 1, 2, 5, 1, 1, 3, 2, 2, 2, 1, 4, 1, 1, 2, 4, 1, 3, 1, 2, 1,
        3, 5, 2, 3, 5, 1, 1, 4, 3, 3, 5, 1, 5, 3, 1, 2, 3, 4, 1, 1, 5, 4, 1, 3, 4, 4, 1, 2, 4, 4, 1, 1, 3, 5, 3, 1, 2,
        2, 5, 1, 4, 1, 3, 3, 3, 3, 1, 1, 2, 1, 5, 3, 4, 5, 1, 5, 2, 5, 3, 2, 1, 4, 2, 1, 1, 1, 4, 1, 2, 1, 2, 2, 4, 5,
        5, 5, 4, 1, 4, 1, 4, 2, 3, 2, 3, 1, 1, 2, 3, 1, 1, 1, 5, 2, 2, 5, 3, 1, 4, 1, 2, 1, 1, 5, 3, 1, 4, 5, 1, 4, 2,
        1, 1, 5, 1, 5, 4, 1, 5, 5, 2, 3, 1, 3, 5, 1, 1, 1, 1, 3, 1, 1, 4, 1, 5, 2, 1, 1, 3, 5, 1, 1, 4, 2, 1, 2, 5, 2,
        5, 1, 1, 1, 2, 3, 5, 5, 1, 4, 3, 2, 2, 3, 2, 1, 1, 4, 1, 3, 5, 2, 3, 1, 1, 5, 1, 3, 5, 1, 1, 5, 5, 3, 1, 3, 3,
        1, 2, 3, 1, 5, 1, 3, 2, 1, 3, 1, 1, 2, 3, 5, 3, 5, 5, 4, 3, 1, 5, 1, 1, 2, 3, 2, 2, 1, 1, 2, 1, 4, 1, 2, 3, 3,
        3, 1, 3, 5]

SPAWNED_FISH_CYCLE = 8
FISH_CYCLE = 6
PART1_DAYS = 80
PART2_DAYS = 256


def make_fish_naive(days: int, ages: List[int]):
    fish = ages.copy()
    for d in range(days):
        # Decrease
        fish = [f - 1 for f in fish]
        # Spawn new fish
        new_fish_count = len([True for f in fish if f == -1])
        fish += [SPAWNED_FISH_CYCLE for _ in range(new_fish_count)]
        # Refresh
        fish = [6 if f == -1 else f for f in fish]
    return len(fish)


# RECURSION DIDN'T WORK :(

# def fish_counting(reproduction_days: int, fish_count: int) -> int:
#     # days_left = first day on which fish is 0
#     if reproduction_days < 0:
#         return fish_count
#     days_left = reproduction_days
#     children_count = 0
#     while days_left > 0:
#         children_count += fish_counting(days_left - SPAWNED_FISH_CYCLE, fish_count)
#         days_left -= FISH_CYCLE
#     return fish_count + children_count
#
#
# def make_fish_counting(days: int, ages: List[int]):
#     m = max(AGES)
#     age_counts = dict([(i, len([True for a in ages if a == i])) for i in range(1, m + 1)])
#     return sum([fish_counting(days - a, c) for a, c in age_counts.items()])

def make_fish_general(days: int, ages: List[int]):
    fish = dict([(i, 0) for i in range(SPAWNED_FISH_CYCLE+2)])
    for a in ages:
        fish[a] += 1

    for d in range(days):
        fish[FISH_CYCLE + 1] += fish[0]
        fish[SPAWNED_FISH_CYCLE + 1] = fish[0]
        fish[0] = 0

        for i in range(SPAWNED_FISH_CYCLE + 1):
            fish[i] = fish[i+1]
        fish[9] = 0

    return sum(fish.values())


print(make_fish_general(PART1_DAYS, AGES))
print(make_fish_general(PART2_DAYS, AGES))
