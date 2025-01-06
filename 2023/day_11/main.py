import re

from utils import get_input_data

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

real_input = get_input_data("2023_day_11.txt")

GalaxyPosition = tuple[int, int]


def func(input_str: str, expansion_factor: int) -> int:
    galaxy_positions: list[GalaxyPosition] = []
    input_lines = input_str.splitlines()
    no_galaxy_rows, no_galaxy_columns = (
        len(input_lines) * [True],
        len(input_lines[0]) * [True],
    )
    for line_idx, line in enumerate(input_str.splitlines()):
        for match in re.finditer(r"#", line):
            col_idx = match.start()
            no_galaxy_rows[line_idx] = False
            no_galaxy_columns[col_idx] = False
            galaxy_positions.append((line_idx, col_idx))

    total_distance = 0
    for left_pair_idx, left_pair in enumerate(galaxy_positions[:-1]):
        for right_pair_idx, right_pair in enumerate(
            galaxy_positions[left_pair_idx + 1 :]
        ):
            total_distance += (
                abs(left_pair[0] - right_pair[0])
                + abs(left_pair[1] - right_pair[1])
                + (expansion_factor - 1)
                * (
                    sum(
                        no_galaxy_rows[
                            min(left_pair[0], right_pair[0]) : max(
                                left_pair[0], right_pair[0]
                            )
                        ]
                    )
                    + sum(
                        no_galaxy_columns[
                            min(left_pair[1], right_pair[1]) : max(
                                left_pair[1], right_pair[1]
                            )
                        ]
                    )
                )
            )
    return total_distance


print("=== V1 - expansion factor 2 ===")
print("Test input : ", func(test_input, 2))
print("Real input : ", func(real_input, 2))

print("\n=== V2 - expansion factor 1M ===")
print("Test input : ", func(test_input, 1_000_000))
print("Real input : ", func(real_input, 1_000_000))
