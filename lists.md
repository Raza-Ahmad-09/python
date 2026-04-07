# Python List Operations – Quick Notes

## Creating a List
```python
tea_varities = ["Black", "Green", "Olong", "White"]

Creates a list with four string elements.

Printing the List
print(tea_varities)

Prints the entire list as-is.

## Indexing

tea_varities[0]

Accesses the first element (index starts from 0).

tea_varities[2]

Accesses the third element.

tea_varities[-1]

Accesses the last element using negative indexing.

## Slicing

tea_varities[1:3]

Returns elements from index 1 up to (but not including) index 3.

tea_varities[:3]

Returns elements from start to index 2.

tea_varities[1:]

Returns elements from index 1 to the end.

tea_varities[:]

Creates a shallow copy of the entire list.

Modifying Elements
tea_varities[3] = "Herbal"

Replaces the element at index 3.

Slice Assignment (Important Concept ⚠️)
tea_varities[1:2] = "Lemon"

Replaces slice with individual characters because a string is iterable.

✅ Better:

tea_varities[1:2] = ["Lemon"]

Replaces slice with a single list element.

Replacing Multiple Elements
tea_varities[1:3] = ["Green", "Masala"]

Replaces multiple elements with new values.

Inserting Without Replacing
tea_varities[1:1] = ["test", "test"]

Inserts elements at index 1 without removing anything.

Deleting Using Slice
tea_varities[1:3] = []

Removes elements from index 1 to 2.

Looping Through List
for tea in tea_varities:
    print(tea)

Iterates through each element.

for tea in tea_varities:
    print(tea, end="-")

Prints elements in one line separated by -.

Checking Membership
if "Oolong" in tea_varities:

Checks if an item exists in the list.

⚠️ Note: "Oolong" vs "Olong" spelling matters.

Adding Elements
tea_varities.append("oolong")

Adds an element at the end.

Removing Elements
tea_varities.pop()

Removes and returns the last element.

tea_varities.remove("Green")

Removes a specific element by value.

Inserting at Specific Position
tea_varities.insert(1, "Green")

Inserts an element at index 1.

Copying a List
tea_varities_copy = tea_varities.copy()

Creates a shallow copy of the list.

List Comprehension
squared_nums = [x**2 for x in range(10)]

Creates a list of squares from 0 to 9.

cube_nums = [y**3 for y in range(5)]

Creates a list of cubes from 0 to 4.

Range Function
range(10)

Generates numbers from 0 to 9 (lazy sequence).
