

# Python Basics (Numbers, Operations & Utilities)

## Variables

```python
x = 2
y = 3
z = 4
Basic Operations
x + y
# 5

⚠️ Avoid unclear expressions:

x + y * z

✔️ Use parentheses for clarity:

(x + y) * z
# 20
Data Types

Avoid mixing types unless intentional:

40 + 2.23
# 42.23

Explicit conversion:

int(2.23)     # 2
float(40)     # 40.0
Operator Overloading
'chai' + 'code'
# 'chaicode'
Multiple Values (Tuples)
x, y, z
# (2, 3, 4)

Operations in tuples:

x + 1, y * 2
# (3, 6)
Arithmetic Operations
y % 2      # 1   (remainder)
z ** 2     # 16  (power)

Large numbers:

2 ** 100
2 ** 1000
repr(), str(), print()
repr('chai')   # "'chai'"
str('chai')    # 'chai'
print('chai')  # chai
repr() → developer/debug view
str() → user-friendly view
print() → outputs to console
Comparisons
1 < 2          # True
5.0 == 5.0     # True
4.0 != 5.0     # True
Chained Comparisons (avoid)
x < y < z

✔️ Better:

x < y and y < z
x < y or y < z
1 == 2 < 3        # False
1 == 2 and 2 < 3  # False
1 == 2 or 2 < 3   # True
Math Module
import math

math.floor(3.5)   # 3
math.floor(-3.5)  # -4
math.trunc(2.8)   # 2
Complex Numbers
2 + 1j
(2 + 1j) * 3
Number Bases
Octal
0o20        # 16
oct(64)     # '0o100'
Hexadecimal
0xFF        # 255
hex(64)     # '0x40'
Binary
0b1000      # 8
bin(64)     # '0b1000000'
Base Conversion
int('64', 8)
Random Module
import random

random.random()
random.randint(1, 10)

l1 = ['lemon', 'masala', 'mint']
random.choice(l1)

random.shuffle(l1)
Floating Point Precision Issue
0.1 + 0.1 + 0.1
# 0.30000000000000004
Solution: Decimal
from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# Decimal('0.3')

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')

Same concept applies to the fractions module.