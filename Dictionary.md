# 🍵 Python Dictionaries — A Chai-Flavored Guide

A **dictionary** is a mutable, ordered collection of key-value pairs. Keys must be unique and immutable.

---

## 📦 Creating a Dictionary

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
```

---

## 🔍 Accessing Values

### By Key (Bracket Notation)
> Direct access — raises `KeyError` if the key doesn't exist.

```python
chai_types["Masala"]   # 'Spicy'
```

### `.get()` — Safe Access
> Returns `None` (or a default) instead of raising an error for missing keys.

```python
chai_types.get("Ginger")    # 'Zesty'
chai_types.get("Gingery")   # None  ← no error, key just doesn't exist
```

> ❌ Dot notation does **not** work on dictionaries:
> ```python
> chai_types.masala  # AttributeError: 'dict' object has no attribute 'masala'
> ```

---

## ✏️ Updating & Adding Entries

> Assigning to an existing key updates it; assigning to a new key creates it.

```python
chai_types["Green"] = "Fresh"   # update existing
chai_types["Earl Grey"] = "Citrus"  # add new key
```

---

## 🔁 Iterating

### Keys Only
> Default iteration gives you only the keys.

```python
for chai in chai_types:
    print(chai)
# Masala
# Ginger
# Green
```

### Keys + Values (Manual)
```python
for chai in chai_types:
    print(chai, chai_types[chai])
```

### `.items()` — Keys & Values Together
> The cleanest, most Pythonic way to loop over both keys and values.

```python
for key, value in chai_types.items():
    print(key, value)
# Masala Spicy
# Ginger Zesty
# Green Fresh
```

---

## ✅ Membership Check

> Use `in` to check if a key exists — fast and readable.

```python
if "Masala" in chai_types:
    print("I have masala chai")
```

---

## 📏 Length

> `len()` returns the number of key-value pairs in the dictionary.

```python
print(len(chai_types))  # 3
```

---

## 🗑️ Removing Entries

### `.pop(key)` — Remove by Key
> Removes the specified key and returns its value.

```python
chai_types.pop("Ginger")   # returns 'Zesty'
```

### `.popitem()` — Remove Last Inserted
> Removes and returns the most recently added key-value pair as a tuple.

```python
chai_types.popitem()   # ('Earl Grey', 'Citrus')
```

### `del` — Delete by Key
> Deletes a key-value pair in-place; raises `KeyError` if key is missing.

```python
del chai_types["Green"]
```

---

## 📋 Copying a Dictionary

> `.copy()` creates a **shallow copy** — changes to the copy won't affect the original.

```python
chai_types_copy = chai_types.copy()
```

---

## 🪆 Nested Dictionaries

> Dictionaries can contain other dictionaries, allowing hierarchical data structures.

```python
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea":  {"Green": "Mild",   "Black": "Strong"}
}

tea_shop["chai"]           # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
tea_shop["chai"]["Ginger"] # 'Zesty'
```

---

## ⚡ Dictionary Comprehension

> Build dictionaries in a single concise line using an expression and an iterable.

```python
squared_num = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🧹 Clearing a Dictionary

> `.clear()` removes all entries, leaving an empty dictionary (the object itself remains).

```python
squared_num.clear()
print(squared_num)  # {}
```

---

## 🏗️ `dict.fromkeys()` — Build from a Key List

> Creates a new dictionary from a list of keys, assigning each the same default value.

```python
keys = ["Masala", "Ginger", "Lemon"]

# With a scalar default
new_dict = dict.fromkeys(keys, "Good")
# {'Masala': 'Good', 'Ginger': 'Good', 'Lemon': 'Good'}

# With a list as default — all keys share the SAME list object
new_dict = dict.fromkeys(keys, keys)
# {'Masala': [...], 'Ginger': [...], 'Lemon': [...]}
```

> ⚠️ **Gotcha:** When the default value is mutable (like a list), all keys point to the **same** object. Modifying one modifies all. Use a comprehension instead if you need independent lists:
> ```python
> new_dict = {k: list(keys) for k in keys}
> ```

---

## 🗂️ Quick Reference

| Method / Operation | Description |
|---|---|
| `d[key]` | Access value; raises `KeyError` if missing |
| `d.get(key)` | Safe access; returns `None` if missing |
| `d[key] = value` | Add or update a key |
| `key in d` | Check if key exists |
| `len(d)` | Number of key-value pairs |
| `d.items()` | Iterate over (key, value) pairs |
| `d.pop(key)` | Remove key, return its value |
| `d.popitem()` | Remove & return last inserted pair |
| `del d[key]` | Delete a key in-place |
| `d.copy()` | Shallow copy of the dictionary |
| `d.clear()` | Remove all entries |
| `dict.fromkeys(keys, val)` | Create dict from a list of keys |
| `{k: expr for k in iterable}` | Dictionary comprehension |