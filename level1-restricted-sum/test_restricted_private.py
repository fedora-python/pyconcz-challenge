import pytest

testdata = [
    [1, 2, 3],
    [2, 2, 2, 2, 2, 2],
    [1, 1, 1],
    [43, -10, 68, 84, 91, 71, -10, -80, 38],
    [42],
    [96, 26, 54, 21, 4],
    [1, 37, -64, 57, -78, 57, 64, -38, -91, 61, 53, -89, 41],
    [42, -24, -74, 96, -62, 5, -47],
    [-55, -66],
    [-30, -53, -2, 73, -27, -62, -49, 17, 99, -10, -31, -73, -67, -31],
    [-34, 46, -22, -65, 92, 23, 99, 82],
    [37, -22, 65, 65, -68, -84, -66, 82, -8, -53, -10, -73],
    [93, 41, -19, -71, 26, -46, 56, -71, -26, 34, 11, -11],
    [-53, 32, 7]
]

forbidden_words = ['sum', 'import', 'for', 'while', 'reduce', 'eval', '__']


@pytest.mark.parametrize("nums", testdata)
def test_restricted(module, nums):
    assert module.restricted(nums) == sum(nums)


@pytest.mark.parametrize("word", forbidden_words)
def test_source_code(module, word):
    with open(module.__file__, 'r') as source_file:
        source_code = source_file.read()

    assert word not in source_code
