with open("input.txt", "r") as input_file:
    input = input_file.readlines()

def parse_card_points(row: str) -> int:
    _, number_info = row.rstrip("\n").split(":")
    winning_numbers, scratched_numbers = number_info.split("|")
    winning_numbers = [num for num in winning_numbers.split(" ") if num != ""]
    scratched_numbers = [num for num in scratched_numbers.split(" ") if num != ""]
    n_common_numbers = sum([scratched_num in winning_numbers for scratched_num in scratched_numbers])
    if n_common_numbers == 0:
        return 0
    return 2 ** (n_common_numbers - 1)

total_points = sum([parse_card_points(row) for row in input])
print(total_points)
