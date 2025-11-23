import pathlib

from pratt_calc.parser import Parser
from pratt_calc.tokenizer import tokenize


def evaluate(raw_expression: str) -> int | float:
    """The proper entry-point into the application.

    Consume RAW_EXPRESSION, and compute a result.

    """

    stream = tokenize(raw_expression)
    parser = Parser(stream)

    value = parser.expression()

    return value


def eval_from_file(filename: str) -> int | float:
    """Consume contents of FILENAME and compute a result."""

    path = pathlib.Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Fatal: '{path}' doesn't exist")

    if path.is_dir():
        raise IsADirectoryError(f"Fatal: '{path}' is a directory")

    with path.open(encoding="utf-8") as f:
        code = f.read()

        return evaluate(code)
