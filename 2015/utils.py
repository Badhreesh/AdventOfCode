from enum import Enum
from pathlib import Path


class Input(Enum):
    DEMO = 1
    GIVEN = 2


def get_input(day: int, _input: Input) -> str:
    file = "demo-input.txt" if _input == Input.DEMO else "input.txt"
    path = Path.cwd() / "inputs" / f"{day}" / file
    return path.read_text()
