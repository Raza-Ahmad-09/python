# Python Tuples Notes

## Creating a Tuple

``` python
tea_types = ("Black", "Green", "Oolong")
tea_types
# ('Black', 'Green', 'Oolong')
```

**Explanation:** A tuple is an ordered, immutable collection of items.

------------------------------------------------------------------------

## Indexing

``` python
tea_types[0]
# 'Black'

tea_types[-1]
# 'Oolong'
```

**Explanation:** Access elements using positive (start) or negative
(end) indexing.

------------------------------------------------------------------------

## Slicing

``` python
tea_types[1:]
# ('Green', 'Oolong')
```

**Explanation:** Extract a portion of the tuple.

------------------------------------------------------------------------

## Immutability

``` python
tea_types[0] = "Lemon"
# TypeError
```

**Explanation:** Tuples cannot be modified after creation.

------------------------------------------------------------------------

## Length

``` python
len(tea_types)
# 3
```

**Explanation:** Returns total number of elements.

------------------------------------------------------------------------

## Tuple Concatenation

``` python
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
# ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
```

**Explanation:** Combines two tuples into one.

------------------------------------------------------------------------

## Membership Test

``` python
"Green" in all_tea
# True
```

**Explanation:** Checks if an element exists in the tuple.

------------------------------------------------------------------------

## Count Method

``` python
more_tea = ("Herbal", "Earl Grey", "Herbal")

more_tea.count("Herbal")
# 2
```

**Explanation:** Counts occurrences of a value in the tuple.

------------------------------------------------------------------------

## Tuple Unpacking

``` python
(black, green, oolong) = tea_types

black   # 'Black'
green   # 'Green'
oolong  # 'Oolong'
```

**Explanation:** Assigns tuple elements to variables.

------------------------------------------------------------------------

## Type Check

``` python
type(tea_types)
# <class 'tuple'>
```

**Explanation:** Confirms the data type is tuple.