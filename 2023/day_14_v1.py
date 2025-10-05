from utils import get_input_data

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

max_rock_score = len(processed_input)
total_score = 0
n_columns = len(processed_input[0])

for col_idx in range(n_columns):
    col_data = "".join(
        [processed_input_row[col_idx] for processed_input_row in processed_input]
    )
    processed_col_data = col_data.split("#")

    current_position = max_rock_score
    for col_split in processed_col_data:
        for _ in range(col_split.count("O")):
            total_score += current_position
            current_position -= 1
        current_position -= col_split.count(".") + 1

print(total_score)
