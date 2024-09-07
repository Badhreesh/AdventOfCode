from enum import Enum
from pathlib import Path


class Input(Enum):
    DEMO = 1
    GIVEN = 2


def get_input(year: int, day: int, _input: Input) -> str:
    file = "demo-input.txt" if _input == Input.DEMO else "input.txt"
    path = Path.cwd() / f"{year}" / "inputs" / f"{day}" / file
    print(path.exists())
    return path.read_text()
