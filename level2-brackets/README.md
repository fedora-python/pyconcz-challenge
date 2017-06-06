# Brackets

You are given an expression with numbers, brackets and operators. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets.

**Input:** An expression with different types of brackets as a `str`.

**Output:** A verdict on the correctness of the expression as a boolean (`True` or `False`).

**Example:**
```python
brackets("((5+3)*2+1)") == True
brackets("{[(3+1)+2]+}") == True
brackets("(3+{1-1)}") == False
```
