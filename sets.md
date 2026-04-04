
# Python Sets & Booleans

## Sets

```python
setone = {1, 2, 3, 4}
Intersection
setone & {1, 3}
# {1, 3}
Union
setone | {1, 3}
# {1, 2, 3, 4}

setone | {1, 3, 7}
# {1, 2, 3, 4, 7}
Original Set
setone
# {1, 2, 3, 4}
Difference
setone - {1, 2, 3, 4}
# set()

⚠️ Empty set uses set() — not {}
{} represents a dictionary

type({})
# <class 'dict'>
Booleans
type(True)
# <class 'bool'>
Comparisons
True == 1
# True

False == 0
# True
Identity (Avoid with literals)
True is 1
# False (and gives a warning)

False is 1
# False

True is 0
# False

⚠️ Use == for value comparison, not is

Boolean Arithmetic
True + 4
# 5

True behaves like 1, and False behaves like 0