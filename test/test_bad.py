import pytest

from pratt_calc.evaluator import Evaluator

bad_examples = [
    "?",
    "(3",
    "()",
    "3/0",
]


@pytest.mark.parametrize("raw_expression", bad_examples)
def test_bad_examples(raw_expression: str):
    with pytest.raises((ValueError, AssertionError, ZeroDivisionError)):
        ev = Evaluator()

        _ = ev.evaluate(raw_expression)
