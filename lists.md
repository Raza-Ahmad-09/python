# 🐍 Python List Operations — Quick Notes

> A **list** is an ordered, mutable collection that can hold mixed data types. Elements are indexed starting from `0`.

---

## 📋 Creating a List

> Define a list using square brackets with comma-separated values.

```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
```

> ⚠️ **Typo fixed throughout:** `"Olong"` → `"Oolong"` and `tea_varities` → `tea_varieties`

---

## 🖨️ Printing a List

> `print()` outputs the entire list including brackets and quotes.

```python
print(tea_varieties)
# ['Black', 'Green', 'Oolong', 'White']
```

---

## 🔍 Indexing

> Access individual elements by their position. Index starts at `0`; negative indices count from the end.

```python
tea_varieties[0]    # 'Black'  ← first element
tea_varieties[2]    # 'Oolong' ← third element
tea_varieties[-1]   # 'White'  ← last element (negative indexing)
```

| Expression | Result | Note |
|---|---|---|
| `tea_varieties[0]` | `'Black'` | First element |
| `tea_varieties[2]` | `'Oolong'` | Third element |
| `tea_varieties[-1]` | `'White'` | Last element |

---

## ✂️ Slicing

> Extract a portion of a list using `[start:stop]`. The `stop` index is **not included**.

```python
tea_varieties[1:3]   # ['Green', 'Oolong'] ← index 1 and 2 only
tea_varieties[:3]    # ['Black', 'Green', 'Oolong'] ← from start to index 2
tea_varieties[1:]    # ['Green', 'Oolong', 'White'] ← index 1 to end
tea_varieties[:]     # ['Black', 'Green', 'Oolong', 'White'] ← shallow copy
```

---

## ✏️ Modifying Elements

> Lists are mutable — you can replace any element directly by index.

```python
tea_varieties[3] = "Herbal"
# ['Black', 'Green', 'Oolong', 'Herbal']
```

---

## ⚠️ Slice Assignment

> Slice assignment replaces a range of elements. Be careful when assigning a **string** — it is iterable and will be broken into individual characters.

```python
# ❌ Incorrect — string is iterable, gets split into characters
tea_varieties[1:2] = "Lemon"
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'White']

# ✅ Correct — wrap in a list to replace as a single element
tea_varieties[1:2] = ["Lemon"]
# ['Black', 'Lemon', 'Oolong', 'White']
```

---

## 🔁 Replacing Multiple Elements

> Assign a list to a slice to replace multiple elements at once.

```python
tea_varieties[1:3] = ["Green", "Masala"]
# ['Black', 'Green', 'Masala', 'White']
```

---

## ➕ Inserting Without Replacing

> Use an empty slice (`[n:n]`) to insert elements at a position without removing anything.

```python
tea_varieties[1:1] = ["Mint", "Jasmine"]
# ['Black', 'Mint', 'Jasmine', 'Green', 'Masala', 'White']
```

---

## 🗑️ Deleting via Slice

> Assign an empty list to a slice to remove elements from that range.

```python
tea_varieties[1:3] = []
# Removes elements at index 1 and 2
```

---

## 🔄 Looping Through a List

> Use a `for` loop to iterate over each element.

```python
# Each element on its own line
for tea in tea_varieties:
    print(tea)

# All elements on one line, separated by '-'
for tea in tea_varieties:
    print(tea, end="-")
# Black-Green-Oolong-White-
```

---

## 🔎 Checking Membership

> Use `in` to check whether an element exists in the list — returns `True` or `False`.

```python
if "Oolong" in tea_varieties:
    print("Oolong is available")
```

> ⚠️ **Spelling matters** — `"Oolong"` and `"Olong"` are treated as completely different strings.

---

## ➕ Adding Elements

> `.append()` adds a single element to the **end** of the list.

```python
tea_varieties.append("Oolong")
# ['Black', 'Green', 'White', 'Oolong']
```

---

## ➕ Inserting at a Specific Position

> `.insert(index, value)` adds an element at the given index, shifting everything after it right.

```python
tea_varieties.insert(1, "Green")
# ['Black', 'Green', 'White', 'Oolong']
```

---

## ❌ Removing Elements

> Two ways to remove: by position (`.pop()`) or by value (`.remove()`).

```python
tea_varieties.pop()             # Removes & returns the last element
tea_varieties.remove("Green")   # Removes the first occurrence of 'Green'
```

| Method | Removes By | Returns | Error If Missing? |
|---|---|---|---|
| `.pop()` | Position (default: last) | The removed element | `IndexError` |
| `.remove(val)` | Value (first match) | `None` | `ValueError` |

---

## 📋 Copying a List

> `.copy()` creates a **shallow copy** — a new list with the same elements. Changes to the copy won't affect the original.

```python
tea_varieties_copy = tea_varieties.copy()
```

---

## ⚡ List Comprehension

> A concise one-line way to build a new list by applying an expression to each item in an iterable.

```python
squared_nums = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_nums = [y**3 for y in range(5)]
# [0, 1, 8, 27, 64]
```

---

## 🔢 `range()`

> `range(n)` generates a lazy sequence of integers from `0` to `n-1`. Commonly used with loops and comprehensions.

```python
range(10)        # 0, 1, 2, ..., 9
list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 📌 Quick Reference

| Operation | Syntax | Notes |
|---|---|---|
| Create | `[a, b, c]` | Mixed types allowed |
| Index | `lst[i]` | Negative index counts from end |
| Slice | `lst[start:stop]` | `stop` is exclusive |
| Shallow copy (slice) | `lst[:]` | Same as `.copy()` |
| Modify element | `lst[i] = val` | In-place |
| Append | `lst.append(val)` | Adds to end |
| Insert | `lst.insert(i, val)` | Shifts elements right |
| Remove by value | `lst.remove(val)` | First match only |
| Remove by position | `lst.pop(i)` | Default: last element |
| Membership test | `val in lst` | Returns `True`/`False` |
| Copy | `lst.copy()` | Shallow copy |
| Comprehension | `[expr for x in iter]` | Concise list building |