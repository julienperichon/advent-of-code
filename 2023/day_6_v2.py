# Result 71503
test_input = """Time:      7  15   30
Distance:  9  40  200"""

# Result 46561107
final_input = """Time:        57     72     69     92
Distance:   291   1172   1176   2026"""

def read_input(input_txt: str) -> tuple[int, int]:
    time_line, distance_line = input_txt.splitlines()
    get_numbers_list = lambda s: int("".join(s.split(":")[1].split()))
    time = get_numbers_list(time_line)
    distance = get_numbers_list(distance_line)
    return (time, distance)

def compute_winning_chances(time_limit: int, dist_record: int) -> int:
    srch_lo, srch_hi = 0, time_limit // 2
    while srch_hi - srch_lo > 1:
        srch_mid = srch_lo + (srch_hi - srch_lo) // 2
        if srch_mid * (time_limit - srch_mid) > dist_record:
            srch_hi = srch_mid
        else:
            srch_lo = srch_mid
    return (time_limit - 1) - 2*srch_lo

# time_limit, dist_record = read_input(test_input)
time_limit, dist_record = read_input(final_input)
winning_chances = compute_winning_chances(time_limit=time_limit, dist_record=dist_record)

print(f"The margin is {winning_chances}")
