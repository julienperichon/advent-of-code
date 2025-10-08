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
) -> int:
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

    return distance - 1


# current_input = test_input_2
current_input = get_input_data("2023_day_10.txt")
processed_input = process_input(current_input)
starting_position = find_starting_position(processed_input)
network = build_network(processed_input, starting_position)

max_distance_from_start = compute_farthest_distance_from_start(
    processed_input, network, starting_position
)
print(max_distance_from_start)
