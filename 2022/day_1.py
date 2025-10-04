from utils import get_input_data_lines

top_elves = 1
input_data = [0]

raw_input_data = get_input_data_lines("2022_day_1.txt")
for line in raw_input_data:
    stripped_line = line.strip()
    if len(stripped_line) > 0:
        input_data[-1] += int(stripped_line)
    else:
        input_data.append(0)

calories_sum = sum(sorted(input_data, reverse=True)[:top_elves])
print(calories_sum)
