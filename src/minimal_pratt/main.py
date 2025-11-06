import enum


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


def expression(tokens: list[Token], i: int, acc: int, level: int) -> tuple[int, int]:
    # NUD
    match tokens[i]:
        case int() as num:
            acc = num
            i += 1

        case _ as token:
            raise ValueError(f"nud: {token}")

    while level < precedence(tokens[i]):
        # LED
        match tokens[i]:
            case "+":
                value, i = expression(tokens, i + 1, acc, Precedence.PLUS_MINUS)
                acc += value

            case "eof":
                pass

            case _ as token:
                raise ValueError(f"led: {token}")

    return acc, i


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

value = expression(t2, 0, 0, Precedence.EOF)

print(value)
