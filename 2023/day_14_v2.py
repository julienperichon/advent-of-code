from pprint import pprint

from file_utils import get_input_data


test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# input_data = test_input
input_data = get_input_data("2023_day_14.txt")
processed_input = input_data.rstrip().split("\n")


def compute_roll_to_right(data: list[str]) -> list[str]:
    new_data: list[str] = []
    for row in data:
        square_rocks_split = row.split("#")
        new_row_parts: list[str] = []
        for square_part in square_rocks_split:
            round_rocks_split = square_part.split("O")
            new_row_parts.append(
                "".join(round_rocks_split) + "O" * (len(round_rocks_split) - 1)
            )
        new_data.append("#".join(new_row_parts))
    return new_data


def rotate_right(data: list[str]) -> list[str]:
    rotated_data: list[str] = []
    n_rows, n_cols = len(data), len(data[0])
    for col_idx in range(n_cols):
        s = ""
        for row_idx in range(n_rows - 1, -1, -1):
            s += data[row_idx][col_idx]
        rotated_data.append(s)
    return rotated_data


def compute_cycled_data(data: list[str]) -> list[str]:
    cycled_data = data
    for _ in range(4):
        cycled_data = compute_roll_to_right(rotate_right(cycled_data))
    return cycled_data


pprint(processed_input)
cycled_data = processed_input

for i in range(10000):
    new_cycled_data = compute_cycled_data(cycled_data)
    if new_cycled_data == cycled_data:
        print(i)
        break
    cycled_data = new_cycled_data
# pprint(cycled_data)
