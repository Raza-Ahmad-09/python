# Object Types / Data Types
Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()

String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'

List : [1, [2, 'three'], 4.5], list(range(10))

Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple

Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

Set : set('abc'), {'a', 'b', 'c'}

File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

Boolean : True, False

None : None

Funtions, modules, classes

Advance: Decorators, Generators, Iterators, MetaProgramming

🔤 String Types
Type	Example
Normal String	'spam'
Double Quotes	"Bob's"
Bytes	b'a\x01c'
Unicode	u'sp\xc4m'
s1 = 'spam'
s2 = "Bob's"
s3 = b'a\x01c'
s4 = u'sp\xc4m'


📋 List
Ordered, mutable collection
my_list = [1, [2, 'three'], 4.5]
numbers = list(range(10))


📦 Tuple
Ordered, immutable collection
t1 = (1, 'spam', 4, 'U')
t2 = tuple('spam')
Named Tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)


📖 Dictionary
Key-value pairs
d1 = {'food': 'spam', 'taste': 'yum'}
d2 = dict(hours=10)
🔗 Set
Unordered, unique elements
s1 = set('abc')
s2 = {'a', 'b', 'c'}


📂 File Handling
f1 = open('eggs.txt')
f2 = open(r'C:\ham.bin', 'wb')
✅ Boolean


is_valid = True
is_done = False
🚫 None Type
x = None

⚙️ Functions
def greet(name):
    return f"Hello, {name}!"


📦 Modules
import math
print(math.sqrt(16))


🏗️ Classes
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"
🚀 Advanced Concepts
🎯 Decorators
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
🔄 Generators
def count_up_to(n):
    for i in range(n):
        yield i
🔁 Iterators
nums = [1, 2, 3]
it = iter(nums)

print(next(it))
🧠 Metaprogramming
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
📌 Notes
Python is dynamically typed.
Everything in Python is an object.
Mutability depends on the data type.