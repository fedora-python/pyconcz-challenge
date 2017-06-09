import pytest
from testdata import testdata


@pytest.mark.parametrize("expresion, result", testdata)
def test_brackets(module, expresion, result):
    assert module.brackets(expresion) == result
