from dataclasses import dataclass
from enum import Enum, auto

from file_utils import get_input_data


test_input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    def __add__(self, point: "Point") -> "Point":
        return Point(row=self.row + point.row, col=self.col + point.col)


Bounce = tuple[Point, Direction]


class Map:
    OOB: str = "out of bounds"

    def __init__(self, data: str) -> None:
        self.data: list[str] = data.rstrip().split("\n")
        self.n_rows: int = len(self.data)
        self.n_cols: int = len(self.data[0])

    def __getitem__(self, key: Point) -> str:
        if not ((0 <= key.row < self.n_rows) and (0 <= key.col < self.n_cols)):
            return Map.OOB
        return self.data[key.row][key.col]


DELTA_POINT_MAPPING = {
    Direction.LEFT: Point(0, -1),
    Direction.RIGHT: Point(0, 1),
    Direction.UP: Point(-1, 0),
    Direction.DOWN: Point(1, 0),
}


def find_next_bounce(input_map: Map, bounce: Bounce) -> list[Bounce]:
    current_point = bounce[0]
    direction = bounce[1]
    delta_point = DELTA_POINT_MAPPING[direction]
    next_bounce_found = False

    while not next_bounce_found:
        current_point = current_point + delta_point
        current_label = input_map[current_point]
        match current_label:
            case Map.OOB:
                return []
            case "|":
                if direction == Direction.LEFT or direction == Direction.RIGHT:
                    return [
                        Bounce((current_point, Direction.UP)),
                        Bounce((current_point, Direction.DOWN)),
                    ]
            case "-":
                if direction == Direction.UP or direction == Direction.DOWN:
                    return [
                        Bounce((current_point, Direction.LEFT)),
                        Bounce((current_point, Direction.RIGHT)),
                    ]
            case "/":
                mapping = {
                    Direction.UP: Direction.RIGHT,
                    Direction.DOWN: Direction.LEFT,
                    Direction.LEFT: Direction.DOWN,
                    Direction.RIGHT: Direction.UP,
                }
                return [Bounce((current_point, mapping[direction]))]
            case "\\":
                mapping = {
                    Direction.UP: Direction.LEFT,
                    Direction.DOWN: Direction.RIGHT,
                    Direction.LEFT: Direction.UP,
                    Direction.RIGHT: Direction.DOWN,
                }
                return [Bounce((current_point, mapping[direction]))]
            case _:
                pass
    return []


def compute_energy_map(input_map: Map, initial_bounce: Bounce) -> list[list[str]]:
    energy_map: list[list[str]] = [
        ["." for _ in range(input_map.n_cols)] for _ in range(input_map.n_rows)
    ]
    current_bounces: list[Bounce] = [initial_bounce]
    visited_bounces: set[Bounce] = set()

    while len(current_bounces) > 0:
        next_bounces: list[Bounce] = []
        for bounce in current_bounces:
            found_bounces = find_next_bounce(input_map, bounce)
            filtered_found_bounces = list(
                filter(lambda b: b not in visited_bounces, found_bounces)
            )
            visited_bounces.update(filtered_found_bounces)
            next_bounces.extend(filtered_found_bounces)

            start_point, end_point = bounce[0], None
            if start_point == initial_bounce[0]:
                start_point = initial_bounce[0] + DELTA_POINT_MAPPING[initial_bounce[1]]
            if len(found_bounces) > 0:
                end_point = found_bounces[0][0]
            else:
                direction = bounce[1]
                end_point = Point(
                    row=(
                        0
                        if direction == Direction.UP
                        else input_map.n_rows - 1
                        if direction == Direction.DOWN
                        else bounce[0].row
                    ),
                    col=(
                        0
                        if direction == Direction.LEFT
                        else input_map.n_cols - 1
                        if direction == Direction.RIGHT
                        else bounce[0].col
                    ),
                )

            if bounce[1] == Direction.LEFT or bounce[1] == Direction.UP:
                start_point, end_point = end_point, start_point
            for row_idx in range(start_point.row, end_point.row + 1):
                for col_idx in range(start_point.col, end_point.col + 1):
                    energy_map[row_idx][col_idx] = "#"

        current_bounces = next_bounces

    return energy_map


def compute_energized_tiles(energy_map: list[list[str]]) -> int:
    return "".join("".join(row) for row in energy_map).count("#")


# used_input = test_input
used_input = get_input_data("2023_day_16.txt")
input_map = Map(used_input)

energy_map = compute_energy_map(
    input_map, initial_bounce=Bounce((Point(0, -1), Direction.RIGHT))
)
# pprint(energy_map)

energized_tiles_count = compute_energized_tiles(energy_map)
print(energized_tiles_count)

print("--------------------")
print("       PART 2       ")
print("--------------------")

record_energized_tiles = 0
record_initial_bounce = None
initial_bounces = (
    [
        Bounce((Point(-1, col_idx), Direction.DOWN))
        for col_idx in range(input_map.n_cols)
    ]
    + [
        Bounce((Point(input_map.n_rows, col_idx), Direction.UP))
        for col_idx in range(input_map.n_cols)
    ]
    + [
        Bounce((Point(row_idx, -1), Direction.RIGHT))
        for row_idx in range(input_map.n_rows)
    ]
    + [
        Bounce((Point(row_idx, input_map.n_cols), Direction.LEFT))
        for row_idx in range(input_map.n_rows)
    ]
)
for initial_bounce in initial_bounces:
    energized_tiles = compute_energized_tiles(
        compute_energy_map(input_map, initial_bounce=initial_bounce)
    )
    if energized_tiles > record_energized_tiles:
        record_energized_tiles = energized_tiles
        record_initial_bounce = initial_bounce

print(f"Best position: {record_initial_bounce} with score {record_energized_tiles}")
