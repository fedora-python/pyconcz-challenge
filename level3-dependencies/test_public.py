import pytest


def test_example1(module):
    pkgs = {
        'cython': [],
        'numpy': {'cython'},
    }

    assert list(module.build_order(pkgs)) == ['cython', 'numpy']


def test_example2(module):
    pkgs = {
        'cython': set(),
        'numpy': ('cython',),
        'fiona': ['cython'],
    }

    result = list(module.build_order(pkgs))

    assert result[0] == 'cython'
    assert set(result) == {'cython', 'fiona', 'numpy'}
    assert len(result) == 3


@pytest.mark.parametrize(
    'pkgs', ({'pip': {'setuptools'}, 'setuptools': {'pip'}},
             {'python': {'magic'}}))
def test_invalid(module, pkgs):
    with pytest.raises(ValueError):
        module.build_order(pkgs)
