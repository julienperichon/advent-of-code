from enum import IntEnum
from pprint import pprint
from typing import NamedTuple, override
from aoc_framework import Solver, Runner

test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


class Range(NamedTuple):
    low: int
    high: int

    @override
    def __contains__(self, key: object, /) -> bool:
        if not isinstance(key, int):
            raise ValueError("key should be int.")
        return self.low <= key <= self.high

    @override
    def __len__(self) -> int:
        return self.high - self.low + 1


class RangeStatus(IntEnum):
    START, STOP = 0, 1


class ProcessedInput(NamedTuple):
    id_ranges: list[Range]
    ids_to_verify: list[int]


class CustomRunner(Runner):
    @override
    def process_input(self, raw_input_data: str) -> ProcessedInput:
        id_ranges_part, ids_to_verify_part = raw_input_data.split("\n\n")
        id_ranges: list[Range] = []
        for line in id_ranges_part.rstrip().splitlines():
            s_low, s_high = line.split("-")
            id_ranges.append(Range(int(s_low), int(s_high)))
        pprint(self.deduplicate_id_ranges(id_ranges))
        return ProcessedInput(
            id_ranges=self.deduplicate_id_ranges(id_ranges),
            ids_to_verify=[
                int(s_id) for s_id in ids_to_verify_part.strip().splitlines()
            ],
        )

    def deduplicate_id_ranges(self, id_ranges: list[Range]) -> list[Range]:
        id_ranges_bounds: list[tuple[int, RangeStatus]] = []
        for id_range in id_ranges:
            id_ranges_bounds.append((id_range.low, RangeStatus.START))
            id_ranges_bounds.append((id_range.high, RangeStatus.STOP))
        id_ranges_bounds = sorted(id_ranges_bounds)

        deduplicated_id_ranges: list[Range] = []
        current_started_ranges: int = 0
        current_lower_bound: int = -1
        for bound in id_ranges_bounds:
            if bound[1] == RangeStatus.START:
                if current_started_ranges == 0:
                    current_lower_bound = bound[0]
                current_started_ranges += 1
            else:
                current_started_ranges -= 1
                if current_started_ranges == 0:
                    deduplicated_id_ranges.append(Range(current_lower_bound, bound[0]))
        return deduplicated_id_ranges


class Part1Solver(Solver):
    def solve(self, processed_input: ProcessedInput) -> int:
        return sum(
            [
                any(
                    [id_to_verify in id_range for id_range in processed_input.id_ranges]
                )
                for id_to_verify in processed_input.ids_to_verify
            ]
        )


class Part2Solver(Part1Solver):
    @override
    def solve(self, processed_input: ProcessedInput) -> int:
        return sum(map(len, processed_input.id_ranges))


CustomRunner(
    solvers=[
        Part1Solver,
        Part2Solver,
    ],
    test_input=test_input,
).run()
