"""
TODO: Fix this
Currently garbage, does not work and computes slowly
"""

import time


def compute_seed_mapping(input: str) -> list[tuple[int]]:
    maps_splitted = input.split("\n\n")
    seed_pairs = list(
        map(
            int,
            maps_splitted[0][len("seeds: "):].split(" ")
        )
    )

    mapping = []
    for idx in range(0, len(seed_pairs), 2):
        mapping.append((seed_pairs[idx], seed_pairs[idx] + seed_pairs[idx + 1], 0))

    for map_i in maps_splitted[1:]:
        prev_mapping, new_mapping = mapping, []
        prev_mapping = sorted(prev_mapping, key=lambda x: x[0] + x[2])
        map_i_lines = map_i.splitlines()
        
        for map_i_line in map_i_lines[1:]:
            dest_range_start, z1, range_len = map(int, map_i_line.split(" "))
            z2 = z1 + range_len
            delta_value = dest_range_start - z1

            for prev_tuple in prev_mapping:
                x1, x2, old_delta = prev_tuple
                y1, y2 = x1 + old_delta, x2 + old_delta
                if z2 <= y1:
                    new_mapping.append((x1, x2, old_delta))
                    break
                if z1 >= y2:
                    new_mapping.append((x1, x2, old_delta))
                elif (z1 <= y1) and (y2 <= z2):
                    new_mapping.append((x1, x2, old_delta + delta_value))
                elif (z1 <= y1 < z2 < y2):
                    new_mapping.append((x1, z2, old_delta + delta_value))
                    new_mapping.append((z2, x2, old_delta))
                elif (y1 < z1 < y2 <= z2):
                    new_mapping.append((x1, z1, old_delta))
                    new_mapping.append((z1, x2, old_delta + delta_value))
                elif (y1 < z1) and (z2 < y2):
                    new_mapping.append((x1, z1, old_delta))
                    new_mapping.append((z1, z2, old_delta + delta_value))
                    new_mapping.append((z2, x2, old_delta))

        mapping = new_mapping
            
    return mapping

with open("input.txt", "r") as input_file:
    input_txt = input_file.read()

# test_input = """seeds: 79 14 55 13
test_input = """seeds: 79 14867 55 13674

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

start = time.time()
seed_mapping = compute_seed_mapping(test_input)
# seed_mapping = compute_seed_mapping(test_input)
closest_seed_mapping = min(seed_mapping, key=lambda x: x[0] + x[2])
print(time.time() - start)
# print(seed_mapping)

print(f"Closest seed is seed {closest_seed_mapping[0]} at distance {closest_seed_mapping[0] + closest_seed_mapping[2]}")
