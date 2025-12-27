import re

from file_utils import get_input_data_lines


def parse_row(row: str) -> int:
    ints = re.sub(r"\D", "", row)
    return int(ints[0] + ints[-1])


def combine_rows(rows: list[str]) -> int:
    return sum(parse_row(row) for row in rows)


rows = get_input_data_lines("2023_day_1.txt")

print(combine_rows(rows))
