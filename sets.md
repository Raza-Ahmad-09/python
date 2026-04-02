>>> setone = {1,2,3,4}
>>> setone & {1,3} -- Intersection 
{1, 3}
>>> setone | {1,3} -- Union
{1, 2, 3, 4}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone - {1,2,3,4} -- difference
set() -- return set but no curly braces, with paranthesis because {} represents dictionary type.
>>> type({})
<class 'dict'>

# Booleans

>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<python-input-80>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> False is 1
<python-input-81>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True is 0
<python-input-82>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 4
5