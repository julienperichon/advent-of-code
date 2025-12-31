from collections.abc import Generator
from typing import override, NamedTuple
from aoc_framework import Solver, Runner

test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


class Point(NamedTuple):
    x: int
    y: int


class Part1Solver(Solver):
    @override
    def solve(self, processed_input: list[str]) -> int:
        masked_input = self._compute_masked_input(processed_input)
        # pprint(masked_input)
        return "".join(masked_input).count("x")

    def _compute_masked_input(self, processed_input: list[str]) -> list[str]:
        masked_input: list[str] = processed_input.copy()
        width, height = len(processed_input[0]), len(processed_input)
        max_positions = Point(height, width)
        for x in range(max_positions.x):
            for y in range(max_positions.y):
                if processed_input[x][y] != "@":
                    continue
                neighbour_statuses = "".join(
                    [
                        processed_input[point.x][point.y]
                        for point in self._generate_neighbour_positions(
                            Point(x, y), max_positions
                        )
                    ]
                )
                if neighbour_statuses.count("@") < 4:
                    masked_input[x] = (
                        masked_input[x][:y] + "x" + masked_input[x][y + 1 :]
                    )
        return masked_input

    def _generate_neighbour_positions(
        self, current_position: Point, max_positions: Point
    ) -> Generator[Point]:
        for x in range(
            max(0, current_position.x - 1),
            min(max_positions.x, current_position.x + 2),
        ):
            for y in range(
                max(0, current_position.y - 1),
                min(max_positions.y, current_position.y + 2),
            ):
                generated_point = Point(x, y)
                if generated_point == current_position:
                    continue
                yield generated_point


class Part2Solver(Part1Solver):
    @override
    def solve(self, processed_input: list[str]) -> int:
        masked_input = processed_input.copy()
        while True:
            new_masked_input = self._compute_masked_input(masked_input)
            if new_masked_input == masked_input:
                break
            masked_input = new_masked_input
        return "".join(masked_input).count("x")


Runner(
    solvers=[
        Part1Solver,
        Part2Solver,
    ],
    test_input=test_input,
).run()
