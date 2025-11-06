import enum
from collections.abc import Callable


class Precedence(enum.IntEnum):
    EOF = enum.auto()
    NONE = enum.auto()
    PLUS_MINUS = enum.auto()
    TIMES_DIVIDE = enum.auto()
    POWER = enum.auto()
    UNARY = enum.auto()


type Token = int | str


def precedence(token: Token) -> Precedence:
    match token:
        case int():
            return Precedence.NONE

        case "eof":
            return Precedence.EOF

        case _:
            raise ValueError(f"Invalid token: '{token}'")


def nud(token: Token) -> Callable[[], int]:
    match token:
        case int() as num:
            return lambda: num

        case _:
            raise ValueError(f"No nud for '{token}'")


def led(token: Token) -> Callable[[int], int]:
    match token:
        case "eof":
            return lambda left: left

        case _:
            raise ValueError(f"No led for '{token}")


def expression(tokens: list[Token], level: int) -> float:
    assert len(tokens) > 1

    h1, h2, *rest = tokens
    value = nud(h1)()

    while level < precedence(h2):
        value = led(h2)(value)

    return value


# The goal is to first parse/evaluate single-number expressions.
#
# And so there are two kinds of token: one with a nud action of
# evaluating to itself, and one with a led action of returning its
# left argument only, and has the lowest binding precedence of all
# tokens.
t1: list[Token] = [3, "eof"]

# Using Precedence.EOF as the starting value of 'level' indicates that
# this is the "primary" level, and by extension the "ground" level for
# expressions.
value = expression(t1, Precedence.EOF)

print(value)
