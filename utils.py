from pathlib import Path

PROJECT_ROOT_FOLDER = Path(__file__).parent.resolve()
INPUT_FOLDER = PROJECT_ROOT_FOLDER / "inputs"


def get_input_data(filename: str) -> str:
    with open(INPUT_FOLDER / filename, "r") as input_file:
        return input_file.read()
