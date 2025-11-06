import enum
from collections.abc import Callable


class Precedence(enum.IntEnum):
    EOF = enum.auto()
    LITERAL = enum.auto()
    PLUS_MINUS = enum.auto()
    TIMES_DIVIDE = enum.auto()
    POWER = enum.auto()
    UNARY = enum.auto()


type Token = int | str


def precedence(token: Token) -> Precedence:
    match token:
        case int():
            return Precedence.LITERAL

        case "+":
            return Precedence.PLUS_MINUS

        case "eof":
            return Precedence.EOF

        case _:
            raise ValueError(f"Invalid token: '{token}'")


def nud(token: Token) -> Callable[[], int]:
    match token:
        case int() as num:
            return lambda: num

        case _ as token:
            raise ValueError(f"No nud for '{token}'")


def led(token: Token, tokens: list[Token]) -> Callable[[int], int]:
    match token:
        case "eof":
            return lambda left: left

        case "+":
            return lambda left: left + expression(tokens, Precedence.PLUS_MINUS)

        case _ as token:
            raise ValueError(f"No led for '{token}")


def expression(tokens: list[Token], level: int) -> int:
    assert len(tokens) > 1
    head, *tokens = tokens

    value = nud(head)()

    while level < precedence(tokens[0]):
        head, *tokens = tokens
        value = led(head, tokens)(value)

    return value


# The goal is to first parse/evaluate single-number expressions.
#
# And so there are two kinds of token: one with a nud action of
# evaluating to itself, and one with a led action of returning its
# left argument only, and has the lowest binding precedence of all
# tokens.

# Using Precedence.EOF as the starting value of 'level' indicates that
# this is the "primary" level, and by extension the "ground" level for
# expressions.

# then let's see how expressions with addition are handled.
t2: list[Token] = [3, "+", 4, "eof"]

value = expression(t2, Precedence.EOF)

print(value)
