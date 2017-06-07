import pytest

testdata = [
    ("((5+3)*2+1)", True),
    ("{[(3+1)+2]+}", True),
    ("(3+{1-1)}", False),
    ("[1+1]+(2*2)-{3/3}", True),
    ("(({[(((1)-2)+3)-3]/3}-3)", False),
]


@pytest.mark.parametrize("expression, result", testdata)
def test_brackets(module, expression, result):
    assert module.brackets(expression) == result
