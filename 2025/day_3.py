from typing import override
from solver_framework import Runner, Solver

test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


class Part1Solver(Solver):
    batteries_to_power_count: int = 2

    @override
    def solve(self, processed_input: list[str]) -> int:
        total_joltage = 0
        for bank_input in processed_input:
            total_joltage += self.get_bank_max_joltage(
                bank_input, n=self.batteries_to_power_count
            )
        return total_joltage

    def get_bank_max_joltage(self, battery_bank: str, n: int) -> int:
        if len(battery_bank) < n:
            raise ValueError
        if n == 0:
            return 0
        bank_len = len(battery_bank)
        n_digit_idx = battery_bank.index(max(battery_bank[: bank_len - n + 1]))
        return int(
            battery_bank[n_digit_idx] + (n - 1) * "0"
        ) + self.get_bank_max_joltage(battery_bank[n_digit_idx + 1 :], n - 1)


class Part2Solver(Part1Solver):
    batteries_to_power_count: int = 12


Runner(
    solvers=[
        Part1Solver,
        Part2Solver,
    ],
    test_input=test_input,
).run()
