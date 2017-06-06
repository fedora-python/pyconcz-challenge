# Restricted sum

From time to time you have to solve some task without your favorite tool or library. To simulate this situation in a simple way, we want you to implement the `sum()` function in a very restricted environment.

Given a list of numbers, you should find the sum of these numbers. The code for your solution should not contain any of the banned words, even as a part of another word.

The list of banned words is as follows:

* sum
* import
* for
* while
* reduce
* eval

**Input:** A list of numbers.

**Output:** The sum of numbers.

**Example:**
```python
restricted([1, 2, 3]) == 6
restricted([2, 2, 2, 2, 2, 2]) == 12
```
