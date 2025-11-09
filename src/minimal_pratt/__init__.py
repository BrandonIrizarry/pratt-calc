import sys
from collections.abc import Callable

from minimal_pratt.parser import Parser
from minimal_pratt.tokenizer import tokenize


def _console(fn: Callable[[str], int]):
    """A wrapper to handle console I/O administrivia."""

    def wrapper(inp: str | None) -> int:
        if inp is None:
            value = fn(sys.argv[1])
        else:
            value = fn(inp)

        print(value)

        return value

    return wrapper


@_console
def main(raw_expression: str) -> int:
    """The proper entry-point into the application.

    Consume RAW_EXPRESSION, and compute an integer result.

    """

    stream = tokenize(raw_expression)
    parser = Parser(stream)

    value = parser.expression()

    return value
