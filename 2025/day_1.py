from typing import override
from solver_framework import Runner, Solver

test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class Part1Solver(Solver):
    def _zero_counter_increment(self, current_position: int, new_position: int) -> int:
        return int((new_position % 100) == 0)

    @override
    def solve(self, processed_input: list[str]) -> int:
        current_position = 50
        zero_counter = 0

        for shift_data in processed_input:
            sign = 2 * (shift_data[0] == "R") - 1
            shift_value = int(shift_data[1:])
            new_position = current_position + sign * shift_value
            increment = self._zero_counter_increment(current_position, new_position)
            zero_counter += increment
            # print(shift_data, current_position, new_position, increment, zero_counter)
            current_position = new_position % 100

        return zero_counter


class Part2Solver(Part1Solver):
    @override
    def _zero_counter_increment(self, current_position: int, new_position: int) -> int:
        if new_position == 0:
            return 1
        if new_position > 0:
            return new_position // 100
        else:
            return abs((new_position - 1) // 100) - (current_position == 0)


Runner(solvers=[Part1Solver, Part2Solver], test_input=test_input).run()
