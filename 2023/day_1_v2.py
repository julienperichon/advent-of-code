import re

from utils import get_input_data_lines

number_correspondance = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_row(row: str) -> int:
    used_row = row
    ints = []
    while len(used_row) > 0:
        if re.match(r"\d", used_row):
            ints.append(used_row[0])
        for key, val in number_correspondance.items():
            if re.match(key, used_row):
                ints.append(val)
        used_row = used_row[1:]
    return int(ints[0] + ints[-1])


rows = get_input_data_lines("2023_day_1.txt")

print(sum(parse_row(row) for row in rows))
