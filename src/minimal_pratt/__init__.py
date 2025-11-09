import sys

from minimal_pratt.parser import Parser
from minimal_pratt.tokenizer import tokenize


def run():
    value = main(sys.argv[1])
    print(value)


def main(raw_expression: str) -> int:
    """The proper entry-point into the application.

    Consume RAW_EXPRESSION, and compute an integer result.

    """

    stream = tokenize(raw_expression)
    parser = Parser(stream)

    value = parser.expression()

    return value
