from math import prod

from utils import get_input_data_lines

LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_row(row: str) -> dict:
    game_id_str, draws_str = row.rstrip("\n").split(": ")
    game_id = int(game_id_str[len("Game ") :])

    min_cube_numbers = {}
    for draw in draws_str.split("; "):
        for color_number_tuple in draw.split(", "):
            number, color = color_number_tuple.split(" ")
            number = int(number)
            if color in min_cube_numbers and min_cube_numbers[color] >= number:
                pass
            else:
                min_cube_numbers[color] = number
    return {"game_id": game_id, "min_cube_numbers": min_cube_numbers}


games = get_input_data_lines("2023_day_2.txt")

total = 0
for game in games:
    game_dict = parse_row(game)
    total += prod([game_dict["min_cube_numbers"][color] for color in LIMITS.keys()])

print(total)
