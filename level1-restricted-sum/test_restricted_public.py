import pytest

testdata = [
    [1, 2, 3],
    [2, 2, 2, 2, 2, 2],
    [1, 1, 1]
]

forbidden_words = ['sum', 'import', 'for', 'while', 'reduce', 'eval']


@pytest.mark.parametrize("nums", testdata)
def test_restricted(module, nums):
    assert module.restricted(nums) == sum(nums)


@pytest.mark.parametrize("word", forbidden_words)
def test_source_code(module, word):
    with open(module.__file__, 'r') as source_file:
        source_code = source_file.read()

    assert word not in source_code
