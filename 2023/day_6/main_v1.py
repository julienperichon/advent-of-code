import math

test_input = """Time:      7  15   30
Distance:  9  40  200"""

final_input = """Time:        57     72     69     92
Distance:   291   1172   1176   2026"""

def read_input(input_txt: str) -> list[tuple[int, int]]:
    time_line, distance_line = input_txt.splitlines()
    get_numbers_list = lambda s: map(int, s.split(":")[1].split())
    times = get_numbers_list(time_line)
    distances = get_numbers_list(distance_line)
    return list(zip(times, distances))

def compute_winning_chances(time_limit: int, dist_record: int) -> int:
    winning_chances = 0
    for trial_time in range(1, time_limit):
        winning_chances += (trial_time * (time_limit - trial_time) > dist_record)
    return winning_chances

time_dist_couples = read_input(final_input)
winning_chances_list = [compute_winning_chances(*time_dist_tuple) for time_dist_tuple in time_dist_couples]

print(f"The margin is {math.prod(winning_chances_list)}")
