from typing import Sequence

with open("input.txt", "r") as input_file:
    input = input_file.readlines()


def count_card_winning_numbers(row: str) -> int:
    _, number_info = row.rstrip("\n").split(":")
    winning_numbers, scratched_numbers = number_info.split("|")
    winning_numbers = [num for num in winning_numbers.split(" ") if num != ""]
    scratched_numbers = [num for num in scratched_numbers.split(" ") if num != ""]
    return sum(
        [scratched_num in winning_numbers for scratched_num in scratched_numbers]
    )


def compute_card_copies(rows: Sequence[str]) -> list[int]:
    card_copies = [1] * len(rows)
    for card_index, card_row in enumerate(rows):
        n_winning_numbers = count_card_winning_numbers(row=card_row)
        for copy_card_index in range(
            card_index + 1, card_index + 1 + n_winning_numbers
        ):
            card_copies[copy_card_index] += card_copies[card_index]
    return card_copies


print(sum(compute_card_copies(input)))
