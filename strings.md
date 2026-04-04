# Python Strings Notes

## Strings

```python
chai = "masala chai"
chai

Explanation: A string is a sequence of characters stored inside quotes.

first_char = chai[0]
first_char

Explanation: Strings support indexing; chai[0] returns the first character.

Slicing of String
chai
slice_chai = chai[0:6]
slice_chai

Explanation: Slicing extracts a portion of the string from index 0 to 5 (6 not included).

num_list = "0123456789"
num_list[:]

Explanation: [:] returns the entire string.

num_list[3:]

Explanation: Returns characters from index 3 to the end.

num_list[:7]

Explanation: Returns characters from start to index 6.

num_list[0:7:2]

Explanation: Third parameter is step; returns every 2nd character.

num_list[0:7:3]

Explanation: Returns every 3rd character in the range.

num_list[0:7:-1]

Explanation: Negative step with forward indices returns empty because direction is invalid.

num_list[0:7:-2]

Explanation: Same as above; step is negative but range is forward.

num_list[0:-7]

Explanation: Returns characters from start to index -8.

Negative Indexing
chai[-1]

Explanation: Negative index accesses characters from the end (-1 is last character).

String Methods
chai = "Lemon chai"
print(chai.lower())

Explanation: Converts all characters to lowercase.

print(chai.upper())

Explanation: Converts all characters to uppercase.

chai1 = "      Masala chai      "
print(chai1.strip())

Explanation: Removes leading and trailing whitespace.

print(chai.replace("Lemon", "Ginger"))

Explanation: Replaces a substring with another value.

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())

Explanation: Splits string by whitespace into a list.

print(chai.split(","))

Explanation: Splits string using comma as delimiter.

chai = "Masala Chai"
print(chai.find("Chai"))

Explanation: Returns index of first occurrence of substring.

print(chai.find("chai"))

Explanation: Returns -1 if substring is not found (case-sensitive).

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

Explanation: Counts occurrences of a substring.

String Formatting
chai_type = "Masala Chai"
quantitiy = 2
order = "I ordered {} cups of {}"
print(order.format(quantitiy, chai_type))

Explanation: format() inserts values into placeholders {}.

Join Method
chai_varitey = ["Lemon","Masala", "Ginger"]
print("".join(chai_varitey))

Explanation: Joins list elements into a string without separator.

print("  ".join(chai_varitey))

Explanation: Joins list elements with spaces.

print("**".join(chai_varitey))

Explanation: Joins list elements with ** as separator.

Length of String
chai = "Masala Chai"
print(len(chai))

Explanation: Returns total number of characters in string.

Looping Through String
for letter in chai:
    print(letter)

Explanation: Iterates over each character in the string.

Escape Characters
chai = "He said, \"Masala chai is awesome\" "

Explanation: Backslash \ is used to escape special characters.

chai = "Masala\n chai"
print(chai)

Explanation: \n creates a new line.

Raw Strings
chai = r"Masala\nchai"
print(chai)

Explanation: Raw strings treat escape sequences as literal text.

path = r"c:\user\pwd"
print(path)

Explanation: Useful for file paths where backslashes are needed.

Membership Operator
chai = "Masala chai"
print("Masala" in chai)

Explanation: Checks if substring exists in string (returns True/False).

print("Masalaa" in chai)

Explanation: Returns False if substring is not present.