from utils import get_input_data

test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# input_data = test_data
input_data = get_input_data("2023_day_9.txt")


def process_input_data(input_data: str) -> list[list[int]]:
    return [
        list(map(int, value_history.split()))
        for value_history in input_data.splitlines()
    ]


# -------------------------
# Part 1
# -------------------------


def predict_next_value(value_history: list[int]) -> int:
    value_history_diffs = [value_history]
    last_value_diff = value_history
    while sum(last_value_diff) != 0:
        value_history_diffs.append(
            [
                last_value_diff[idx] - last_value_diff[idx - 1]
                for idx in range(1, len(last_value_diff))
            ]
        )
        last_value_diff = value_history_diffs[-1]

    next_value = 0
    for value_diff in value_history_diffs[::-1][1:]:
        next_value += value_diff[-1]
    return next_value


sum_next_values = 0
for value_history in process_input_data(input_data):
    sum_next_values += predict_next_value(value_history)

print(f"Result part 1: {sum_next_values}")

# -------------------------
# Part 2
# -------------------------


def predict_previous_value(value_history: list[int]) -> int:
    value_history_diffs = [value_history]
    last_value_diff = value_history
    while sum(last_value_diff) != 0:
        value_history_diffs.append(
            [
                last_value_diff[idx] - last_value_diff[idx - 1]
                for idx in range(1, len(last_value_diff))
            ]
        )
        last_value_diff = value_history_diffs[-1]

    previous_value = 0
    for value_diff in value_history_diffs[::-1][1:]:
        previous_value = value_diff[0] - previous_value
    return previous_value


sum_previous_values = 0
for value_history in process_input_data(input_data):
    sum_previous_values += predict_previous_value(value_history)

print(f"Result part 2: {sum_previous_values}")
