from utils import get_input_data


def compute_seed_mapping(input: str) -> list[list[int]]:
    maps_splitted = input.split("\n\n")
    seeds = map(int, maps_splitted[0][len("seeds: ") :].split(" "))
    mapping = [[seed_id] for seed_id in seeds]

    for map_i in maps_splitted[1:]:
        map_i_lines = map_i.splitlines()

        mapping = [[*sublist, sublist[-1]] for sublist in mapping]
        for map_i_line in map_i_lines[1:]:
            dest_range_start, src_range_start, range_len = map(
                int, map_i_line.split(" ")
            )

            for seed_mapping in mapping:
                if (seed_mapping[-2] >= src_range_start) and (
                    seed_mapping[-2] < src_range_start + range_len
                ):
                    seed_mapping[-1] = dest_range_start + (
                        seed_mapping[-2] - src_range_start
                    )
    return mapping


input_txt = get_input_data("2023_day_5.txt")

seed_mapping = compute_seed_mapping(input_txt)
closest_seed_mapping = min(seed_mapping, key=lambda x: x[-1])

print(
    f"Closest seed is seed {closest_seed_mapping[0]} at distance {closest_seed_mapping[-1]}"
)
