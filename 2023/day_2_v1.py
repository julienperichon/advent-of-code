from utils import get_input_data_lines


LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_row(row: str) -> dict:
    game_id_str, draws_str = row.rstrip("\n").split(": ")
    game_id = int(game_id_str[len("Game ") :])

    draws = []
    for draw in draws_str.split("; "):
        draw_cubes_info = {}
        for color_number_tuple in draw.split(", "):
            number, color = color_number_tuple.split(" ")
            draw_cubes_info[color] = int(number)
        draws.append(draw_cubes_info)

    return {"game_id": game_id, "draws": draws}


def check_row_feasibility(game_dict: dict) -> tuple[int, bool]:
    is_game_feasible = True

    for draw in game_dict["draws"]:
        for color, number in draw.items():
            if number > LIMITS[color]:
                is_game_feasible = False
                break

    return game_dict["game_id"], is_game_feasible


games = get_input_data_lines("2023_day_2.txt")

total = 0
for game in games:
    game_dict = parse_row(game)
    game_id, feasibility = check_row_feasibility(game_dict)
    total += feasibility * game_id

print(total)
