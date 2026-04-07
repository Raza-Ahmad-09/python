# 🐍 Python Basics — Numbers, Operations & Utilities

> Python handles numbers, arithmetic, type conversion, and math utilities in a clean and expressive way. This guide covers everything from basic operations to floating-point precision fixes.

---

## 📦 Variables

> Variables in Python are created on assignment — no type declaration needed.

```python
x = 2
y = 3
z = 4
```

---

## ➕ Basic Operations

> Python supports all standard arithmetic operators. Operator precedence follows standard math rules (`*` before `+`).

```python
x + y       # 5

# ⚠️ Ambiguous — multiplication happens before addition
x + y * z   # 14, not 20

# ✅ Use parentheses to make intent explicit
(x + y) * z  # 20
```

---

## 🔢 Data Types & Conversion

> Python automatically promotes integers to floats when mixed, but explicit conversion gives you control.

```python
# Implicit type promotion
40 + 2.23    # 42.23 (int + float → float)

# Explicit conversion
int(2.23)    # 2    ← truncates, does NOT round
float(40)    # 40.0
```

> ⚠️ `int()` always **truncates** toward zero — it does not round. Use `round()` for rounding.

---

## 🔗 Operator Overloading

> The `+` operator works on strings too — it concatenates them.

```python
'chai' + 'code'    # 'chaicode'
'chai' * 3         # 'chaichaichai' ← repetition with *
```

---

## 📦 Multiple Values & Tuples

> Multiple variables on one line implicitly form a tuple.

```python
x, y, z        # (2, 3, 4)

# Operations on tuple expressions
x + 1, y * 2   # (3, 6)
```

---

## ⚙️ Arithmetic Operations

> Python provides `%` for remainder and `**` for exponentiation. Both work on arbitrarily large numbers.

```python
y % 2       # 1  ← remainder (modulo)
z ** 2      # 16 ← exponentiation (z to the power of 2)

# Python handles arbitrarily large integers natively
2 ** 100    # 1267650600228229401496703205376
2 ** 1000   # (a very large number — no overflow!)
```

---

## 🖨️ `repr()`, `str()`, and `print()`

> Three different ways to display values — each suited to a different context.

```python
repr('chai')    # "'chai'"  ← includes quotes; developer/debug view
str('chai')     # 'chai'    ← clean string; user-friendly view
print('chai')   #  chai     ← outputs to console, no quotes
```

| Function | Output Style | Best Used For |
|---|---|---|
| `repr()` | Unambiguous, with type hints | Debugging, logging |
| `str()` | Readable, human-friendly | Display to users |
| `print()` | Writes directly to console | General output |

---

## ⚖️ Comparisons

> Comparison operators return `True` or `False`.

```python
1 < 2           # True
5.0 == 5.0      # True
4.0 != 5.0      # True
```

---

## 🔗 Chained Comparisons

> Python supports chained comparisons, but explicit `and`/`or` is clearer for complex logic.

```python
# ⚠️ Works, but can be surprising in complex expressions
x < y < z

# ✅ Explicit and readable
x < y and y < z
x < y or  y < z
```

```python
# How Python evaluates chained logic
1 == 2 < 3          # False → (1 == 2) is False, short-circuits
1 == 2 and 2 < 3    # False → same result, explicit
1 == 2 or  2 < 3    # True  → second condition (2 < 3) is True
```

---

## 📐 Math Module

> The `math` module provides mathematical functions beyond basic arithmetic.

```python
import math

math.floor(3.5)    #  3 ← rounds DOWN to nearest integer
math.floor(-3.5)   # -4 ← floor goes more negative, not toward zero
math.trunc(2.8)    #  2 ← strips decimal, always toward zero
math.sqrt(16)      #  4.0
math.pi            #  3.141592653589793
```

| Function | Result | Behaviour |
|---|---|---|
| `math.floor(3.5)` | `3` | Always rounds down |
| `math.floor(-3.5)` | `-4` | Down = more negative |
| `math.trunc(2.8)` | `2` | Truncates toward zero |
| `round(2.5)` | `2` | Banker's rounding (rounds to even) |

---

## 🔭 Complex Numbers

> Python has built-in complex number support using `j` for the imaginary unit.

```python
2 + 1j            # (2+1j)
(2 + 1j) * 3      # (6+3j)
(2 + 1j).real     # 2.0 ← real part
(2 + 1j).imag     # 1.0 ← imaginary part
```

---

## 🔢 Number Bases

> Python supports octal, hexadecimal, and binary literals natively, and provides functions to convert between them.

### Octal (Base 8)

```python
0o20        # 16  ← octal literal
oct(64)     # '0o100'
```

### Hexadecimal (Base 16)

```python
0xFF        # 255 ← hex literal
hex(64)     # '0x40'
```

### Binary (Base 2)

```python
0b1000      # 8   ← binary literal
bin(64)     # '0b1000000'
```

### Base Conversion with `int()`

> `int(string, base)` converts a number string from any base to a decimal integer.

```python
int('64', 8)    # 52  ← reads '64' as octal
int('FF', 16)   # 255 ← reads 'FF' as hex
int('1000', 2)  # 8   ← reads '1000' as binary
```

---

## 🎲 `random` Module

> Provides functions for generating random numbers and making random choices.

```python
import random

random.random()           # Random float between 0.0 and 1.0
random.randint(1, 10)     # Random integer between 1 and 10 (inclusive)

l1 = ['lemon', 'masala', 'mint']
random.choice(l1)         # Picks one element at random
random.shuffle(l1)        # Shuffles the list in-place (modifies l1)
```

| Function | Returns | Modifies Original? |
|---|---|---|
| `random.random()` | Float in `[0.0, 1.0)` | — |
| `random.randint(a, b)` | Int in `[a, b]` | — |
| `random.choice(seq)` | One random element | No |
| `random.shuffle(seq)` | `None` | ✅ Yes (in-place) |

---

## 🎯 Floating Point Precision

> Floats are stored in binary and cannot represent all decimal values exactly — a fundamental limitation of IEEE 754 floating-point arithmetic.

```python
0.1 + 0.1 + 0.1
# 0.30000000000000004  ← not a Python bug, a hardware limitation
```

### ✅ Fix: Use `Decimal`

> `Decimal` stores numbers as exact decimal values, eliminating binary rounding errors.

```python
from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# Decimal('0.3')  ✅ exact

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')  ✅ no floating-point drift
```

> ⚠️ Always pass `Decimal` a **string** (`'0.1'`), not a float (`0.1`) — otherwise the imprecision is baked in before `Decimal` even sees it.

### ✅ Alternative: Use `Fraction`

> `Fraction` stores numbers as exact rationals (numerator/denominator) — useful for mathematical precision.

```python
from fractions import Fraction

Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10)
# Fraction(3, 10)  ← exactly 3/10
```

---

## 📌 Quick Reference

| Operation | Syntax | Notes |
|---|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Use `()` for clarity |
| Integer division | `//` | Floors the result |
| Modulo | `%` | Returns remainder |
| Power | `**` | Handles huge numbers |
| Type conversion | `int()`, `float()`, `str()` | `int()` truncates |
| Comparisons | `<`, `>`, `==`, `!=`, `<=`, `>=` | Return `bool` |
| Math utilities | `import math` | `floor`, `trunc`, `sqrt`, `pi` |
| Random | `import random` | `choice`, `shuffle`, `randint` |
| Exact decimals | `from decimal import Decimal` | Pass strings, not floats |
| Exact fractions | `from fractions import Fraction` | Stores as `a/b` |