import typer
from pathlib import Path

def main(input_file_path: Path = typer.Option(...), top_elves: int = typer.Option(1)) -> None:
    input_data = [0]
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                input_data[-1] += int(stripped_line)
            else:
                input_data.append(0)

    calories_sum = sum(sorted(input_data, reverse=True)[:top_elves])
    print(calories_sum)

if __name__ == "__main__":
    typer.run(main)
