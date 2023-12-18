import re

number_correspondance = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
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

with open("input.txt", "r") as input_file:
    rows = input_file.readlines()

print(sum(parse_row(row) for row in rows))
