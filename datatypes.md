# 🐍 Python Object & Data Types — Complete Guide

> Everything in Python is an **object**. Python is dynamically typed — you don't declare types, Python infers them at runtime.

---

## 🗺️ Overview

| Type | Examples |
|---|---|
| **Number** | `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()` |
| **String** | `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'` |
| **List** | `[1, [2, 'three'], 4.5]`, `list(range(10))` |
| **Tuple** | `(1, 'spam', 4, 'U')`, `tuple('spam')`, `namedtuple` |
| **Dictionary** | `{'food': 'spam', 'taste': 'yum'}`, `dict(hours=10)` |
| **Set** | `set('abc')`, `{'a', 'b', 'c'}` |
| **File** | `open('eggs.txt')`, `open(r'C:\ham.bin', 'wb')` |
| **Boolean** | `True`, `False` |
| **None** | `None` |
| **Callable** | Functions, Modules, Classes |
| **Advanced** | Decorators, Generators, Iterators, Metaprogramming |

---

## 🔢 Numbers

> Python supports integers, floats, complex numbers, binary literals, and arbitrary-precision types.

```python
i  = 1234          # Integer
f  = 3.1415        # Float
c  = 3 + 4j        # Complex number
b  = 0b111         # Binary literal (= 7)

from decimal import Decimal
from fractions import Fraction

d  = Decimal('0.1')       # Exact decimal arithmetic (no floating-point errors)
fr = Fraction(1, 3)       # Exact rational arithmetic
```

---

## 🔤 Strings

> Strings are immutable sequences of characters. Python supports multiple literal forms for different use cases.

```python
s1 = 'spam'       # Standard string
s2 = "Bob's"      # Double quotes — useful when the string contains a single quote
s3 = b'a\x01c'    # Bytes literal — raw binary data, not text
s4 = u'sp\xc4m'   # Unicode string (u-prefix is optional in Python 3)
```

| Type | Example | Use Case |
|---|---|---|
| Normal | `'spam'` | Everyday text |
| Double-quoted | `"Bob's"` | Contains a single quote |
| Bytes | `b'a\x01c'` | Binary data / network protocols |
| Unicode | `u'sp\xc4m'` | Internationalised text |

---

## 📋 Lists

> Ordered, **mutable** collection — elements can be added, removed, or changed after creation.

```python
my_list = [1, [2, 'three'], 4.5]   # Can mix types and nest lists
numbers  = list(range(10))          # [0, 1, 2, ..., 9]
```

---

## 📦 Tuples

> Ordered, **immutable** collection — once created, elements cannot be changed.

```python
t1 = (1, 'spam', 4, 'U')   # Standard tuple
t2 = tuple('spam')          # ('s', 'p', 'a', 'm') — built from an iterable
```

### Named Tuple
> Gives each position a name, making tuple fields self-documenting and accessible by name.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)   # 10 20
```

---

## 📖 Dictionaries

> Unordered (Python 3.7+ insertion-ordered) collection of **key-value pairs**. Keys must be unique and immutable.

```python
d1 = {'food': 'spam', 'taste': 'yum'}   # Literal syntax
d2 = dict(hours=10)                      # Keyword argument syntax → {'hours': 10}
```

---

## 🔗 Sets

> Unordered collection of **unique** elements — duplicates are automatically removed.

```python
s1 = set('abc')    # {'a', 'b', 'c'} — built from an iterable
s2 = {'a', 'b', 'c'}  # Set literal syntax
```

> ⚠️ Use `set()` for an empty set — `{}` creates an empty **dict**, not a set.

---

## 📂 File Handling

> `open()` returns a file object for reading and writing. Always close files (or use `with`).

```python
f1 = open('eggs.txt')              # Open text file for reading
f2 = open(r'C:\ham.bin', 'wb')     # Open binary file for writing (raw string avoids escape issues)

# Preferred — automatically closes the file even if an error occurs
with open('eggs.txt') as f:
    content = f.read()
```

---

## ✅ Booleans

> `True` and `False` are instances of `int` (`True == 1`, `False == 0`). Used for logic and control flow.

```python
is_valid = True
is_done  = False

print(True + True)   # 2 — booleans are ints under the hood
```

---

## 🚫 None

> `None` is Python's null value — a singleton representing the absence of a value.

```python
x = None

print(x is None)   # True ← always use `is` to check for None, not `==`
```

---

## ⚙️ Functions

> Reusable blocks of code defined with `def`. Functions are first-class objects in Python.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Chai"))   # Hello, Chai!
```

---

## 📦 Modules

> A module is a `.py` file that groups related functions, classes, and variables for reuse.

```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592653589793
```

---

## 🏗️ Classes

> Classes are blueprints for creating objects. They bundle data (attributes) and behaviour (methods) together.

```python
class Person:
    def __init__(self, name):
        self.name = name        # Instance attribute

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Arham")
print(p.greet())   # Hi, I'm Arham
```

---

## 🚀 Advanced Concepts

### 🎯 Decorators

> A decorator wraps a function to extend or modify its behaviour without changing its source code.

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function call
# Hello!
# After function call
```

---

### 🔄 Generators

> A generator yields values one at a time using `yield`, pausing execution between calls — memory-efficient for large sequences.

```python
def count_up_to(n):
    for i in range(n):
        yield i

for num in count_up_to(5):
    print(num)   # 0, 1, 2, 3, 4
```

---

### 🔁 Iterators

> Any object with `__iter__()` and `__next__()` methods. `iter()` and `next()` let you traverse it manually.

```python
nums = [1, 2, 3]
it   = iter(nums)

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it) now raises StopIteration
```

---

### 🧠 Metaprogramming

> Metaclasses control how **classes themselves** are created — a class whose instances are classes.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
# Output: Creating class: MyClass
```

---

## 📌 Key Takeaways

| Concept | Detail |
|---|---|
| **Dynamic typing** | Types are checked at runtime, not compile time |
| **Everything is an object** | Functions, classes, and modules are objects too |
| **Mutability** | `list`, `dict`, `set` are mutable; `str`, `tuple`, `int` are immutable |
| **None check** | Always use `is None`, never `== None` |
| **Empty set** | Use `set()`, not `{}` (that's an empty dict) |