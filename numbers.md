>>> x = 2
>>> y = 3
>>> z = 4
<!--  they are the normal mathematical operations such including others (-,*,/,**,//) -->
>>> x + y
5
<!-- But this thing must be noticed not like x + y * z, this should be avoided or if necessary must use paranthesis as give below -->
>>> (x + y) * z
20
<!-- Also make sure don't use mismatched datatypes like one is int and other one is float -->
>>> 40 + 2.23
42.23
<!-- if its necessary then your intension must be clear that what you want to do here as give  -->
>>> int(2.23)
2
or
>>> float(40)
40.0

<!-- python also has operator overloading, mean automatically decides what on left or right, other progamming languages also have this its not a rocket science -->
>>> 'chai' + 'code'
'chaicode'

<!-- if we call more than one variables in one line it return a tuple -->
>>> x , y, z
(2, 3, 4)


<!-- similarly it also can perform operations -->
>>> x + 1, y * 2
(3, 6)


<!-- we can also find remainder and so on -->
>>> y % 2
1
>>> z ** 2
16


<!-- python is much more powerful in number calculations even it doesn't crashes on large numbers -->
>>> 100 ** 2
10000
>>> 2 ** 100
1267650600228229401496703205376
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376


Use repr() → for debugging, gives an unambiguous, developer-oriented string (often recreatable)
Use str() → for user-friendly display, returns a clean and readable version of the object
Use print() → for outputting to console, automatically calls str() on objects and handles formatting like spaces and newlines

>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai

<!-- --------------------------------------------------- COMPARISONS --------------------------------------------------------- -->

" <  > >=  <="
-- It returns boolean

>>> 1 < 2
True

>>> 5.0 ==  5.0
True

>>> 4.0 != 5.0
True

# Chained Comparisons
>>> x < y < z -- Not a good practice
True


>>> x < y and y < z -- here the keyword and used (satisfy both conditions)
True
>>> x < y or y < z --- here keyword or used (satisfy one or both conditions)
Ture

>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
>>> 1 == 2 or 2 < 3
True

# Some operations

>>> import math -- as library
>>> math.floor(3.5) -- floor returns lower number
3
>>> math.floor(-3.5)
-4
>>> math.trunc(2.8) -- trunc returns number close to zero
2

# Imaginary Numbers

>>> 2 + 1j
(2+1j)
>>> (2 + 1j) * 3
(6+3j)

# Octal base

>>> 0o20 -- always start with 0o {zero O}
16
>>> oct(64)
'0o100'
# Hex base

>>> 0xFF -- always start with 0x
255
>>> hex(64)
'0x40'

# Binary literals

>>> 0b1000 -- start with 0b
8
 >>> bin(64)
'0b1000000'


<!-- method trick -->
int('number', base)

int('64', 8)


# Random Library

>>> import random

>>> random.random()
0.5746369280683362
>>> random.random()
0.9654730309127271

>>> random.randint(1,10)
7
>>> random.randint(1,10)
6
>>> random.randint(1,10)
8
>>> random.randint(1,10)
9

>>> l1 = ['lemon','masala','mint']

>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'masala'

>>> random.shuffle(l1)
>>> random.shuffle(l1)

# Decimal Problem 

>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1 
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17

<!-- import decimal for this  -->
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

<!-- same scene with Fractions -->

