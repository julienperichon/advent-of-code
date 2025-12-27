# test_input = """RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""
from file_utils import get_input_data

test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def process_input(input_str: str) -> tuple[str, dict[str, dict[str, str]]]:
    splitted_input = input_str.splitlines()
    instructions = splitted_input[0]
    graph = {
        node_info[:3]: {"L": node_info[7:10], "R": node_info[12:15]}
        for node_info in splitted_input[2:]
    }
    return instructions, graph


def run_instructions_once(
    starting_node: str, instructions: str, graph: dict[str, dict[str, str]]
) -> str:
    current_node = starting_node
    for instruction in instructions:
        current_node = graph[current_node][instruction]
    return current_node


input_data = get_input_data("2023_day_8.txt")
instructions, graph = process_input(input_data)
current_node = "AAA"
runs_count = 0
while current_node != "ZZZ":
    current_node = run_instructions_once(current_node, instructions, graph)
    runs_count += 1

print(runs_count * len(instructions))
