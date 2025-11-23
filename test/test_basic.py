import pytest

from pratt_calc.main import evaluate

# The original set of examples, before floats were introduced.
basic = [
    ("3", 3),
    ("3 + 4", 7),
    ("3 + 4 * 5 + 6", 29),
    ("3 + -4 * 5 + 6", -11),
    ("-3 + 4", 1),
    ("(3 + -4) * 5 + 6", 1),
    ("2^3^2", 512),
    ("2^3*3", 24),
    ("2^(3*2)", 64),
    ("2-3*2", -4),
    ("-(3 + 1)!", -24),
    ("(3)", 3),
    ("- 3", -3),
]


@pytest.mark.parametrize("raw_expression, value", basic)
def test_basic(raw_expression: str, value: int):
    result = evaluate(raw_expression)

    assert result == value
