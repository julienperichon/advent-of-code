import re
from typing import Sequence

def parse_row(row: str) -> int:
    ints = re.sub(r"\D", "", row)
    return int(ints[0] + ints[-1])

def combine_rows(rows: Sequence[str]) -> int:
    return sum(parse_row(row) for row in rows)

with open("input.txt", "r") as input_file:
    rows = input_file.readlines()

print(combine_rows(rows))
