from utils import get_input_data


test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def hash_algorithm(s: str) -> int:
    val = 0
    for char in s:
        val = (val + ord(char)) * 17 % 256
    return val


assert hash_algorithm("rn=1") == 30
assert hash_algorithm("cm-") == 253
assert hash_algorithm("qp=3") == 97
assert hash_algorithm("cm=2") == 47
assert hash_algorithm("qp-") == 14
assert hash_algorithm("pc=4") == 180
assert hash_algorithm("ot=9") == 9
assert hash_algorithm("ab=5") == 197
assert hash_algorithm("pc-") == 48
assert hash_algorithm("pc=6") == 214
assert hash_algorithm("ot=7") == 231

# current_input = test_input
current_input = get_input_data("2023_day_15.txt")
total_score = sum(
    [hash_algorithm(substring) for substring in current_input.rstrip().split(",")]
)
print(total_score)
