from enum import Enum, auto
from utils import get_input_data


test_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

test_input_2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

Point = tuple[int, int]
Network = dict[Point, list[Point]]


def process_input(input_data: str) -> list[str]:
    return input_data.rstrip().split("\n")


def find_starting_position(processed_input: list[str]) -> Point:
    for row_idx, row in enumerate(processed_input):
        for col_idx, char in enumerate(row):
            if char == "S":
                return (row_idx, col_idx)
    return (-1, -1)


def build_network(processed_input: list[str], starting_point: Point) -> Network:
    network: Network = {}
    for row_idx, row in enumerate(processed_input):
        for col_idx, char in enumerate(row):
            neighbours: list[Point] = []
            match char:
                case "|":
                    neighbours = [(row_idx - 1, col_idx), (row_idx + 1, col_idx)]
                case "-":
                    neighbours = [(row_idx, col_idx - 1), (row_idx, col_idx + 1)]
                case "L":
                    neighbours = [(row_idx - 1, col_idx), (row_idx, col_idx + 1)]
                case "J":
                    neighbours = [(row_idx - 1, col_idx), (row_idx, col_idx - 1)]
                case "7":
                    neighbours = [(row_idx, col_idx - 1), (row_idx + 1, col_idx)]
                case "F":
                    neighbours = [(row_idx, col_idx + 1), (row_idx + 1, col_idx)]
                case _:
                    continue
            network[(row_idx, col_idx)] = neighbours
            if starting_point in neighbours:
                network[starting_point] = [
                    *network.get(starting_point, []),
                    (row_idx, col_idx),
                ]

    return network


def compute_farthest_distance_from_start(
    processed_input: list[str], network: Network, starting_position: Point
) -> tuple[int, list[list[str]]]:
    loop_display = [
        [" " for _ in range(len(processed_input[0]))]
        for _ in range(len(processed_input))
    ]
    points_to_explore = [starting_position]
    distance = 0

    while len(points_to_explore) > 0:
        new_points_to_explore = []
        for point in points_to_explore:
            loop_display[point[0]][point[1]] = "#"
            for neighbour in network[point]:
                if loop_display[neighbour[0]][neighbour[1]] != "#":
                    new_points_to_explore.append(neighbour)
        points_to_explore = new_points_to_explore
        distance += 1

    return distance - 1, loop_display


def compute_raw_loop_without_starting_point(
    processed_input: list[str], network: Network, starting_position: Point
) -> list[str]:
    new_processed_input = processed_input.copy()
    neighbour1, neighbour2 = network[starting_position]
    if neighbour1[0] > neighbour2[0] or neighbour1[1] > neighbour2[1]:
        neighbour1, neighbour2 = neighbour2, neighbour1

    real_starting_point_char = None
    if neighbour1[1] == starting_position[1] - 1:
        if neighbour2[0] == starting_position[0] - 1:
            real_starting_point_char = "J"
        elif neighbour2[0] == starting_position[0]:
            real_starting_point_char = "-"
        else:
            real_starting_point_char = "7"
    elif neighbour1[1] == neighbour2[1]:
        real_starting_point_char = "|"
    else:
        if neighbour1[0] == starting_position[0] - 1:
            real_starting_point_char = "L"
        else:
            real_starting_point_char = "F"

    old = new_processed_input[starting_position[0]]
    new = (
        old[: starting_position[1]]
        + real_starting_point_char
        + old[starting_position[1] + 1 :]
    )
    new_processed_input[starting_position[0]] = new
    return new_processed_input


class EnclosingStatus(Enum):
    OUTSIDE = auto()
    INSIDE = auto()
    TRANSITION_FROM_OUTSIDE = auto()
    TRANSITION_FROM_INSIDE = auto()


def compute_enclosed_tiles(
    loop_display: list[list[str]], processed_input: list[str]
) -> tuple[list[list[str]], int]:
    new_loop_display = loop_display.copy()
    enclosed_tiles = 0
    transition_opening_char = None
    for row_idx, row in enumerate(processed_input):
        current_status = EnclosingStatus.OUTSIDE
        for col_idx, char in enumerate(row):
            corrected_char = char if loop_display[row_idx][col_idx] == "#" else "."
            # print(row_idx, col_idx, corrected_char, current_status)
            if current_status == EnclosingStatus.INSIDE:
                if corrected_char == ".":
                    enclosed_tiles += 1
                    new_loop_display[row_idx][col_idx] = "I"
                elif corrected_char == "|":
                    current_status = EnclosingStatus.OUTSIDE
                else:
                    transition_opening_char = corrected_char
                    current_status = EnclosingStatus.TRANSITION_FROM_INSIDE
            elif current_status == EnclosingStatus.OUTSIDE:
                if corrected_char == "|":
                    current_status = EnclosingStatus.INSIDE
                elif corrected_char != ".":
                    transition_opening_char = corrected_char
                    current_status = EnclosingStatus.TRANSITION_FROM_OUTSIDE
            else:
                is_uturn = (
                    transition_opening_char == "F" and corrected_char == "7"
                ) or (transition_opening_char == "L" and corrected_char == "J")
                is_zigzag = (
                    transition_opening_char == "F" and corrected_char == "J"
                ) or (transition_opening_char == "L" and corrected_char == "7")

                if is_uturn:
                    transition_opening_char = None
                    current_status = (
                        EnclosingStatus.INSIDE
                        if current_status == EnclosingStatus.TRANSITION_FROM_INSIDE
                        else EnclosingStatus.OUTSIDE
                    )
                if is_zigzag:
                    transition_opening_char = None
                    current_status = (
                        EnclosingStatus.INSIDE
                        if current_status == EnclosingStatus.TRANSITION_FROM_OUTSIDE
                        else EnclosingStatus.OUTSIDE
                    )
    return new_loop_display, enclosed_tiles


# current_input = test_input
current_input = get_input_data("2023_day_10.txt")
processed_input = process_input(current_input)
starting_position = find_starting_position(processed_input)
network = build_network(processed_input, starting_position)

max_distance_from_start, loop_display = compute_farthest_distance_from_start(
    processed_input, network, starting_position
)
# pprint(loop_display)
print(max_distance_from_start)

new_processed_input = compute_raw_loop_without_starting_point(
    processed_input, network, starting_position
)
loop_display_with_enclosed_tiles, num_enclosed_tiles = compute_enclosed_tiles(
    loop_display, new_processed_input
)
# pprint(loop_display_with_enclosed_tiles)
print(num_enclosed_tiles)
