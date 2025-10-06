from functools import cache

from utils import get_input_data


test_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def process_input(input_data: str) -> tuple[list[str], list[tuple[int, ...]]]:
    spring_data: list[str] = []
    arrangement_data: list[tuple[int, ...]] = []
    for row in input_data.rstrip().split("\n"):
        springs, arrangement = row.split(" ")
        spring_data.append(springs)
        arrangement_data.append(tuple([int(x) for x in arrangement.split(",")]))
    return (spring_data, arrangement_data)


def subproblem_from_hole(spring_data: str, target_arrangement: tuple[int, ...]) -> int:
    return compute_row_valid_arrangements(spring_data[1:], target_arrangement)


def subproblem_from_spring(
    spring_data: str, target_arrangement: tuple[int, ...]
) -> int:
    spring_group = spring_data[: target_arrangement[0]]
    if "." in spring_group:
        return 0
    if (
        len(spring_data) > target_arrangement[0]
        and spring_data[target_arrangement[0]] == "#"
    ):
        return 0

    return compute_row_valid_arrangements(
        spring_data[target_arrangement[0] + 1 :], target_arrangement[1:]
    )


@cache
def compute_row_valid_arrangements(
    spring_data: str, target_arrangement: tuple[int, ...]
) -> int:
    if len(spring_data) < sum(target_arrangement) + len(target_arrangement) - 1:
        return 0
    if len(target_arrangement) == 0:
        if "#" in spring_data:
            return 0
        return 1
    if len(spring_data) == 0:
        return 0

    current_char = spring_data[0]
    if current_char == ".":
        return subproblem_from_hole(spring_data, target_arrangement)
    if current_char == "#":
        return subproblem_from_spring(spring_data, target_arrangement)

    return subproblem_from_hole(
        spring_data, target_arrangement
    ) + subproblem_from_spring(spring_data, target_arrangement)


# input_data = test_input
input_data = get_input_data("2023_day_12.txt")
spring_data, arrangement_data = process_input(input_data)
total_score = 0
for row, arrangement in zip(spring_data, arrangement_data):
    total_score += compute_row_valid_arrangements(row, arrangement)

print(total_score)
