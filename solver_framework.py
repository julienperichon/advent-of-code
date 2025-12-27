from abc import ABC, abstractmethod
from pathlib import Path
import re
from typing import Annotated, Any
import typer
import __main__

from file_utils import PROJECT_ROOT_FOLDER, get_input_data


def get_input_path_from_module_path(module_path: Path) -> str:
    relative_module_path = module_path.relative_to(PROJECT_ROOT_FOLDER)
    year = str(relative_module_path.parent.name)
    day = re.findall(r"(day_)(\d+)(.*\.py)", relative_module_path.name)[0][1]
    return f"{year}_day_{day}.txt"


class Solver(ABC):
    @abstractmethod
    def solve(self, processed_input: list[str]) -> Any:
        pass


class Runner:
    def __init__(self, solvers: list[type[Solver]], test_input: str = "") -> None:
        self.solvers: list[type[Solver]] = solvers

        if not hasattr(__main__, "__file__"):
            raise Exception("Error while detecting input file path.")
        self._real_input_filename: str = get_input_path_from_module_path(
            Path(__main__.__file__)
        )
        self._test_input: str = test_input

    def run(self):
        typer.run(self._run)

    def _run(
        self, using_test_input: Annotated[bool, typer.Option("--test")] = False
    ) -> None:
        raw_input_data: str = (
            self._test_input
            if using_test_input
            else get_input_data(self._real_input_filename)
        )
        processed_input = self.process_input(raw_input_data)

        for solver in self.solvers:
            solution = solver().solve(processed_input)
            print(solver.__name__, solution)

    def process_input(self, raw_input_data: str) -> list[str]:
        return raw_input_data.rstrip().splitlines()
