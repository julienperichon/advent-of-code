from utils import get_input_data


test_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def process_input(input: str) -> list[list[str]]:
    patterns = input.split("\n\n")
    processed_input: list[list[str]] = []
    for pat in patterns:
        processed_input.append(pat.rstrip().split("\n"))
    return processed_input


def invert_pattern(pattern: list[str]) -> list[str]:
    inverted_pattern = [""] * len(pattern[0])
    for line in pattern:
        for i, char in enumerate(line):
            inverted_pattern[i] += char
    return inverted_pattern


def check_symmetry_axis(pattern: list[str], potential_symmetry_axis: int) -> bool:
    n_rows = len(pattern)
    lb, ub = (
        max(0, n_rows - 2 * (n_rows - potential_symmetry_axis)),
        min(n_rows, 2 * potential_symmetry_axis),
    )
    before_axis = "".join(pattern[lb:potential_symmetry_axis][::-1])
    after_axis = "".join(pattern[potential_symmetry_axis:ub])
    return sum([before_axis[i] != after_axis[i] for i in range(len(before_axis))]) == 1


def find_horizontal_symmetry_axes(pattern: list[str]) -> int:
    """Return number of rows before found horizontal symmetry axis."""
    n_rows = len(pattern)
    for potential_symmetry_axis in range(1, n_rows):
        if check_symmetry_axis(pattern, potential_symmetry_axis):
            return potential_symmetry_axis
    return 0


def find_all_horizontal_axes(patterns: list[list[str]]) -> list[int]:
    horizontal_axes: list[int] = []
    for pattern in patterns:
        horizontal_axes.append(find_horizontal_symmetry_axes(pattern))
    return horizontal_axes


def find_all_vertical_axes(patterns: list[list[str]]) -> list[int]:
    vertical_axes: list[int] = []
    for pattern in patterns:
        vertical_axes.append(find_horizontal_symmetry_axes(invert_pattern(pattern)))
    return vertical_axes


input_data = get_input_data("2023_day_13.txt")
# input_data = test_input
processed_input = process_input(input_data)
horizontal_axes = find_all_horizontal_axes(processed_input)
vertical_axes = find_all_vertical_axes(processed_input)

print(100 * sum(horizontal_axes) + sum(vertical_axes))
