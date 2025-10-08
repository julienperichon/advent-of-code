from utils import get_input_data


test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def hash_algorithm(s: str) -> int:
    val = 0
    for char in s:
        val = (val + ord(char)) * 17 % 256
    return val


Lens = tuple[str, int]


def find_lens_index(linked_list: list[Lens], lens_label: str) -> int | None:
    index = 0
    for lens in linked_list:
        if lens[0] == lens_label:
            return index
        index += 1
    return None


def parse_substring(substring: str) -> tuple[str, str, int | None]:
    if substring[-1] == "-":
        return substring[:-1], "-", None

    label, focal_length = substring.split("=")
    return label, "=", int(focal_length)


def hashmap_algorithm(s: str) -> int:
    hashmap = {}
    for substring in s.rstrip().split(","):
        label, type, focal_length = parse_substring(substring)
        lens_bucket = hash_algorithm(label)
        linked_list: list[Lens] = hashmap.get(lens_bucket, [])
        current_lens_index = find_lens_index(linked_list, label)
        if type == "=":
            if current_lens_index is None:
                linked_list.append((label, focal_length))
            else:
                linked_list[current_lens_index] = (label, focal_length)
        else:
            if current_lens_index is not None:
                linked_list.pop(current_lens_index)
        hashmap[lens_bucket] = linked_list

    total_score = 0
    for bucket, linked_list in hashmap.items():
        for index, lens in enumerate(linked_list):
            total_score += (bucket + 1) * (index + 1) * lens[1]
    return total_score


# current_input = test_input
current_input = get_input_data("2023_day_15.txt")
print(hashmap_algorithm(current_input))
