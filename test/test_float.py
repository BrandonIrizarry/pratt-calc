import math

import pytest

from pratt_calc.main import evaluate

float_examples = [
    ("3.3", 3.3),
    ("3.3+4.4", 7.7),
    ("5/2", 2.5),
    ("1+5/2", 3.5),
    ("100*(100 + 1)/2", 5050),
    ("pi", math.pi),
    ("sin (pi/2)", 1),
    ("sin(pi/2)^2 + cos(pi/2)^2", 1),
    ("tan(pi/4)", 1),
    ("1 + 0.5", 1.5),
    ("1 + tan(pi/4)", 1 / math.pow(math.cos(math.pi / 4), 2)),
    ("sin(1)^2", 0.7080734182735712),
    ("sin 1^2", 0.7080734182735712),
    ("1 + cot(1)^2 - csc(1)^2", 0),
    ("1 + tan(1)^2 - sec(1)^2", 0),
]


@pytest.mark.parametrize("raw_expression, value", float_examples)
def test_float_examples(raw_expression: str, value: int | float):
    result = evaluate(raw_expression)

    assert math.isclose(result, value, abs_tol=1e-10)
