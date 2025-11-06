import pytest

from minimal_pratt.main import Precedence, Token, expression

examples = [([3, "eof"], 3), ([0, "eof"], 0), ([3, "+", 4, "eof"], 7)]


@pytest.mark.parametrize("tokens, value", examples)
def test_examples(tokens: list[Token], value: int):
    result, _ = expression(tokens, 0, 0, Precedence.EOF)

    assert result == value
