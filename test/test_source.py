import math

import pytest

from pratt_calc.main import eval_from_file

examples = [
    ("test/source.txt", 20),
]


@pytest.mark.parametrize("filename, value", examples)
def test_examples(filename: str, value: int | float):
    result = eval_from_file(filename)

    assert math.isclose(result, value, abs_tol=1e-10)
