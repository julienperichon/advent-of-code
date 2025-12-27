# TODO: Does not work yet, but apparently do some LCM
import time

from file_utils import get_input_data
from statistics import mean, stdev

test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

Graph = dict[str, dict[str, str]]


def process_input(input_str: str) -> tuple[str, Graph]:
    splitted_input = input_str.splitlines()
    instructions = splitted_input[0]
    graph = {
        node_info[:3]: {"L": node_info[7:10], "R": node_info[12:15]}
        for node_info in splitted_input[2:]
    }
    return instructions, graph


def get_starting_nodes(graph: Graph) -> list[str]:
    return [key for key in graph.keys() if key[-1] == "A"]


def run_instruction_on_nodes(
    current_nodes: list[str], instruction: str, graph: Graph
) -> list[str]:
    return [graph[node][instruction] for node in current_nodes]


def is_path_end(current_nodes: list[str]) -> bool:
    return all([node[-1] == "Z" for node in current_nodes])


def compute_loop(
    starting_node: str, instructions: list[str], graph: Graph
) -> list[str]:
    node_list = [starting_node]
    for inst in instructions:
        new_node = graph[node_list[-1]][inst]
        node_list.append(new_node)
    node_list.append(graph[node_list[-1]][instructions[0]])
    return node_list


# input_data = test_input
input_data = get_input_data("2023_day_8.txt")

instructions, graph = process_input(input_data)
current_nodes = get_starting_nodes(graph)

runs_count = 0
instructions_count = len(instructions)
is_path_end_var = False
run_instructions_times = []
is_path_end_times = []
while not is_path_end_var and runs_count < 1000000:
    t0 = time.time()
    current_nodes = run_instruction_on_nodes(
        current_nodes, instructions[runs_count % instructions_count], graph
    )
    t1 = time.time()
    is_path_end_var = is_path_end(current_nodes)
    t2 = time.time()
    run_instructions_times.append(t1 - t0)
    is_path_end_times.append(t2 - t1)
    runs_count += 1

print(runs_count)
print(mean(run_instructions_times), stdev(run_instructions_times))
print(mean(is_path_end_times), stdev(is_path_end_times))
