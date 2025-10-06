from utils import get_input_data


test_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def process_input(input_data: str) -> tuple[list[str], list[list[int]]]:
    spring_data: list[str] = []
    arrangement_data: list[list[int]] = []
    for row in input_data.rstrip().split("\n"):
        springs, arrangement = row.split(" ")
        spring_data.append(springs)
        arrangement_data.append([int(x) for x in arrangement.split(",")])
    return (spring_data, arrangement_data)


def compute_active_arrangement(spring_row: str) -> list[int]:
    return list(filter(lambda x: x > 0, map(len, spring_row.split("."))))


def compute_row_valid_arrangements(
    spring_data: str, target_arrangement: list[int]
) -> int:
    valid_arrangements = [""]
    for char in spring_data:
        if char == "?":
            valid_arrangements = [
                *[s + "#" for s in valid_arrangements],
                *[s + "." for s in valid_arrangements],
            ]
        else:
            valid_arrangements = [s + char for s in valid_arrangements]

    total_target_arrangements = 0
    for arrangement in valid_arrangements:
        total_target_arrangements += (
            compute_active_arrangement(arrangement) == target_arrangement
        )
    return total_target_arrangements


input_data = get_input_data("2023_day_12.txt")
spring_data, arrangement_data = process_input(input_data)
total_score = 0
for row, arrangement in zip(spring_data, arrangement_data):
    total_score += compute_row_valid_arrangements(row, arrangement)

print(total_score)
