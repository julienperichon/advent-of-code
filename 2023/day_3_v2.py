import re
from math import prod
from itertools import product
from typing import Optional

from utils import get_input_data_lines


def find_matches_in_row(row: str, pattern: str) -> list[re.Match]:
    return list(re.finditer(pattern, row))


parse_numbers = lambda row: find_matches_in_row(row, r"\d+")
parse_symbols = lambda row: find_matches_in_row(row, r"[^\d\.]")

rows = get_input_data_lines("2023_day_3.txt")

rows = [row.rstrip("\n") for row in rows]
N_LINES = len(rows)

number_matches = [parse_numbers(row) for row in rows]
symbol_matches = [parse_symbols(row) for row in rows]


def search_match_at_col_index(
    matches: list[re.Match], col_index: int
) -> Optional[re.Match]:
    for match in matches:
        if match.start() <= col_index and col_index < match.end():
            return match
    return None


def get_gears(
    symbol_matches: list[list[re.Match]], number_matches: list[list[re.Match]]
) -> list[list[re.Match]]:
    gears = []
    for line_index, line_symbols_matches in enumerate(symbol_matches):
        for symbol_match in line_symbols_matches:
            symbol_col_index = symbol_match.start()
            line_indexes = set(
                [max(line_index - 1, 0), line_index, min(line_index + 1, N_LINES - 1)]
            )
            col_indexes = [symbol_col_index - 1, symbol_col_index, symbol_col_index + 1]
            gear_matches = []
            for line_idx, col_idx in product(line_indexes, col_indexes):
                m = search_match_at_col_index(number_matches[line_idx], col_idx)
                if m is not None and m not in gear_matches:
                    gear_matches.append(m)
            if len(gear_matches) == 2:
                gears.append(gear_matches)

    return gears


def compute_total(gears: list[list[re.Match]]) -> int:
    return sum(prod(int(m.group()) for m in gear_numbers) for gear_numbers in gears)


gears = get_gears(symbol_matches, number_matches)
print(gears)
print(compute_total(gears))
