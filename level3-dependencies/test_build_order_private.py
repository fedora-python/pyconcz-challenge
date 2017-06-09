import pytest


def is_valid_result(pkgs, result):
    built = {pkg: False for pkg in pkgs}
    for pkg in result:
        if pkg not in built:
            print(f'{pkg} was not supposed to be built at all')
            return False
        if built[pkg]:
            print(f'{pkg} already built')
            return False
        for dependency in pkgs[pkg]:
            if not built[dependency]:
                print(f'{pkg} needs {dependency} but that was not yet built')
                return False
        built[pkg] = True
    for key, value in built.items():
        if not value:
            print(f'{key} not built at the end')
            return False
    return True


VALIDS = [
    {
        'a': ['b', 'c', 'd'],
        'b': ['d'],
        'c': ['d'],
        'd': [],
    },
    {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': ['f'],
        'f': [],
        'g': [],
    },
    {
        '.': [],
        'a': ['.'],
        'b': ['.', 'a'],
        'c': ['.', 'a', 'b'],
        'd': ['.', 'a', 'b', 'c'],
    },
    {
        '.': [],
    },
]

INVALIDS = [
    {
        'a': ['a'],
    },
    {
        'a': ['nonexistent'],
    },
    {
        'a': ['b'],
        'b': ['c'],
        'c': ['d'],
        'd': ['a'],
    },
]


@pytest.mark.parametrize('pkgs', VALIDS)
def test_valids(module, pkgs):
    assert is_valid_result(pkgs, module.build_order(pkgs))


@pytest.mark.parametrize('pkgs', INVALIDS)
def test_invalids(module, pkgs):
    with pytest.raises(ValueError):
        module.build_order(pkgs)
