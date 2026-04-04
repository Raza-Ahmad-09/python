# Strings

>>> chai = "masala chai"
>>> chai
'masala chai'
<!-- In python strings can also be considered as a list so we can assess characters as in array(indexing) -->
>>> first_char = chai[0]
>>> first_char
'm'

# Slicing of string
>>> chai
'masala chai'
<!-- 0 is starting index and 6 is last index which is not included it means it returs the results form 0 to 5 -->
>>> slice_chai = chai[0:6]
>>> slice_chai
'masala'
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
<!-- here third param is hoping condition -->
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'
>>> num_list[0:7:-1]
''
>>> num_list[0:7:-2]
''
>>> num_list[0:-7]
'012

# Negative indexing
>>> chai[-1]
'i'

# Strings Methods