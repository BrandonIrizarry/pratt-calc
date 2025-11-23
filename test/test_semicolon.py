import math

import pytest

from pratt_calc.main import evaluate

semicolon_examples = [
    ("3 ; 4", 4),
    ("3 + 4 ; 4 + 5", 9),
    ("1 ; 2 ; 3 ; 4", 4),
]


@pytest.mark.parametrize("raw_expression, value", semicolon_examples)
def test_semicolon_examples(raw_expression: str, value: int | float):
    result = evaluate(raw_expression)

    assert math.isclose(result, value, abs_tol=1e-10)
