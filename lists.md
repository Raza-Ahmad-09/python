# Python List Operations – Quick Notes

# Creating a List
- ```python
  tea_varieties = ["Black", "Green", "Oolong", "White"]
Creates a list with four string elements.
Printing the List
print(tea_varieties)
Prints the entire list.
Indexing
tea_varieties[0]
Accesses the first element (index starts from 0).
tea_varieties[2]
Accesses the third element.
tea_varieties[-1]
Accesses the last element using negative indexing.
Slicing
tea_varieties[1:3]
Returns elements from index 1 to 2.
tea_varieties[:3]
Returns elements from start to index 2.
tea_varieties[1:]
Returns elements from index 1 to the end.
tea_varieties[:]
Returns a shallow copy of the list.
Modifying Elements
tea_varieties[3] = "Herbal"
Replaces the element at index 3.
Slice Assignment (Important ⚠️)
tea_varieties[1:2] = "Lemon"
Splits string into characters because strings are iterable.

✅ Better:

tea_varieties[1:2] = ["Lemon"]
Correct way to insert a single item.
Replacing Multiple Elements
tea_varieties[1:3] = ["Green", "Masala"]
Replaces multiple elements with new values.
Inserting Without Replacing
tea_varieties[1:1] = ["test", "test"]
Inserts elements at index 1 without deleting anything.
Deleting Using Slice
tea_varieties[1:3] = []
Removes elements from index 1 to 2.
Looping Through List
for tea in tea_varieties:
    print(tea)
Iterates through each element.
for tea in tea_varieties:
    print(tea, end="-")
Prints elements in one line separated by -.
Checking Membership
if "Oolong" in tea_varieties:
Checks if an item exists in the list.
Adding Elements
tea_varieties.append("Oolong")
Adds an element at the end.
Removing Elements
tea_varieties.pop()
Removes and returns the last element.
tea_varieties.remove("Green")
Removes a specific element by value.
Inserting at Specific Position
tea_varieties.insert(1, "Green")
Inserts an element at index 1.
Copying a List
tea_varieties_copy = tea_varieties.copy()
Creates a shallow copy of the list.
List Comprehension
squared_nums = [x**2 for x in range(10)]
Creates a list of squares from 0 to 9.
cube_nums = [y**3 for y in range(5)]
Creates a list of cubes from 0 to 4.
Range Function
range(10)
Generates numbers from 0 to 9.