from aoc_framework import Solver, Runner
from typing import override

test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


class CustomRunner(Runner):
    @override
    def process_input(self, raw_input_data: str) -> list[tuple[int, int]]:
        ranges = raw_input_data.rstrip().split(",")
        processed_input: list[tuple[int, int]] = []
        for id_range in ranges:
            s_low, s_high = id_range.split("-")
            processed_input.append((int(s_low), int(s_high)))
        return processed_input


class Part1Solver(Solver):
    def find_invalid_ids_in_range(self, low: int, high: int) -> list[int]:
        invalid_ids: list[int] = []
        for num in range(low, high + 1):
            snum = str(num)
            snum_len = len(snum)
            if snum_len % 2 != 0:
                continue
            if snum[: snum_len // 2] == snum[snum_len // 2 :]:
                invalid_ids.append(num)
        return invalid_ids

    @override
    def solve(self, processed_input: list[tuple[int, int]]) -> int:
        invalid_ids: list[int] = []
        for low, high in processed_input:
            invalid_ids.extend(self.find_invalid_ids_in_range(low, high))
        return sum(invalid_ids)


PRIME_NUMBERS = [2, 3, 5, 7, 11]


class Part2Solver(Part1Solver):
    def split_into_same_string_length_intervals(
        self, low: int, high: int
    ) -> list[tuple[int, int]]:
        same_slen_intervals: list[tuple[int, int]] = []
        for num_length in range(len(str(low)), len(str(high)) + 1):
            new_low = "1" + (num_length - 1) * "0"
            new_high = num_length * "9"
            used_low = max(low, int(new_low))
            used_high = min(high, int(new_high))
            same_slen_intervals.append((used_low, used_high))
        return same_slen_intervals

    @override
    def find_invalid_ids_in_range(self, low: int, high: int) -> list[int]:
        invalid_ids: set[int] = set()
        split_ranges = self.split_into_same_string_length_intervals(low, high)
        for split_low, split_high in split_ranges:
            for prime in PRIME_NUMBERS:
                id_len = len(str(split_low))
                if id_len // prime == 0 or id_len % prime != 0:
                    continue
                min_repeat_num, max_repeat_num = (
                    split_low // 10 ** (id_len - id_len / prime),
                    split_high // 10 ** (id_len - id_len / prime),
                )
                min_repeat_num, max_repeat_num = (
                    int(min_repeat_num),
                    int(max_repeat_num),
                )
                invalid_ids_candidates: list[int] = []
                for repeat_num in range(min_repeat_num, max_repeat_num + 1):
                    invalid_ids_candidates.append(int(str(repeat_num) * prime))
                invalid_ids.update(
                    filter(
                        lambda x: split_low <= x <= split_high, invalid_ids_candidates
                    )
                )

        # print(low, high, sorted(invalid_ids))

        return list(invalid_ids)


CustomRunner(solvers=[Part1Solver, Part2Solver], test_input=test_input).run()
