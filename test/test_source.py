import math

import pytest

from pratt_calc.evaluator import Evaluator

examples = [
    ("test/source.txt", 20),
    ("test/source_comments.txt", 15),
]


@pytest.mark.parametrize("filename, value", examples)
def test_examples(filename: str, value: int | float):
    ev = Evaluator()
    result = ev.evaluate_file(filename)

    assert math.isclose(result, value, abs_tol=1e-10)
