# Build Order

You are given a dictionary with packages. Each package has an iterable (list, tuple, iterator, set...) of its dependencies. Your task is to return an ordered iterable (i.e. no set) with their build order. A dependency must always be built before the package that depends on it.

Sometimes, multiple solutions exist (in reality some packages may be built in parallel),
in that case any valid solution is good.

**Input:** `dict` with `str` as keys and iterables of `str`s as values.

**Output:** ordered iterable with `str`s.

**Raises:** `ValueError` if dependencies cannot be met.

**Example:**
```python

pkgs = {
    'cython': [],
    'numpy': {'cython'},
}

build_order(pkgs) => ['cython', 'numpy']
```

```python
pkgs = {
    'cython': set(),
    'numpy': ('cython',),
    'fiona': ['cython'],
}

build_order(pkgs) => ['cython', 'numpy', 'fiona'] or ('cython', 'fiona', 'numpy')
```

```python
pkgs = {
    'pip': {'setuptools'},
    'setuptools': {'pip'},
}

build_order(pkgs) raises ValueError
```

```python
build_order({'python': {'magic'}}) raises ValueError
```


