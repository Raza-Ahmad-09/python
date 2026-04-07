# Python Sets & Booleans Notes

## Sets

``` python
setone = {1, 2, 3, 4}
```

------------------------------------------------------------------------

## Intersection

``` python
setone & {1, 3}
# {1, 3}
```

**Explanation:** Returns common elements between sets.

------------------------------------------------------------------------

## Union

``` python
setone | {1, 3}
# {1, 2, 3, 4}

setone | {1, 3, 7}
# {1, 2, 3, 4, 7}
```

**Explanation:** Combines elements from both sets (no duplicates).

------------------------------------------------------------------------

## Original Set

``` python
setone
# {1, 2, 3, 4}
```

------------------------------------------------------------------------

## Difference

``` python
setone - {1, 2, 3, 4}
# set()
```

**Explanation:** Removes matching elements.

------------------------------------------------------------------------

## Empty Set Warning

``` python
set()
```

⚠️ Empty set uses `set()` --- not `{}`

``` python
type({})
# <class 'dict'>
```

**Explanation:** `{}` creates a dictionary, not a set.

------------------------------------------------------------------------

## Booleans

``` python
type(True)
# <class 'bool'>
```

------------------------------------------------------------------------

## Comparisons

``` python
True == 1
# True

False == 0
# True
```

**Explanation:** `True` behaves like `1`, `False` like `0`.

------------------------------------------------------------------------

## Identity (Avoid with literals)

``` python
True is 1
# False

False is 1
# False

True is 0
# False
```

⚠️ Use `==` for value comparison, not `is`.

------------------------------------------------------------------------

## Boolean Arithmetic

``` python
True + 4
# 5
```

**Explanation:** `True = 1`, `False = 0`.