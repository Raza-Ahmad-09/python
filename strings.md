# Python Strings Notes

## Strings

``` python
chai = "masala chai"
chai
```

**Explanation:** A string is a sequence of characters stored inside
quotes.

``` python
first_char = chai[0]
first_char
```

**Explanation:** Strings support indexing; `chai[0]` returns the first
character.

------------------------------------------------------------------------

## Slicing of String

``` python
slice_chai = chai[0:6]
slice_chai
```

**Explanation:** Extracts characters from index 0 to 5.

``` python
num_list = "0123456789"
num_list[:]
```

**Explanation:** Returns entire string.

``` python
num_list[3:]
```

**Explanation:** From index 3 to end.

``` python
num_list[:7]
```

**Explanation:** From start to index 6.

``` python
num_list[0:7:2]
```

**Explanation:** Step of 2.

``` python
num_list[0:7:3]
```

**Explanation:** Step of 3.

``` python
num_list[0:7:-1]
```

**Explanation:** Invalid direction → empty.

``` python
num_list[0:-7]
```

**Explanation:** From start to index -8.

------------------------------------------------------------------------

## Negative Indexing

``` python
chai[-1]
```

**Explanation:** Last character.

------------------------------------------------------------------------

## String Methods

``` python
chai = "Lemon chai"
chai.lower()
chai.upper()
```

``` python
chai1 = "      Masala chai      "
chai1.strip()
```

``` python
chai.replace("Lemon", "Ginger")
```

``` python
chai = "Lemon, Ginger, Masala, Mint"
chai.split()
chai.split(",")
```

``` python
chai = "Masala Chai"
chai.find("Chai")
chai.find("chai")
```

``` python
chai = "Masala Chai Chai Chai"
chai.count("Chai")
```

------------------------------------------------------------------------

## String Formatting

``` python
chai_type = "Masala Chai"
quantity = 2
order = "I ordered {} cups of {}"
order.format(quantity, chai_type)
```

------------------------------------------------------------------------

## Join Method

``` python
chai_variety = ["Lemon","Masala","Ginger"]
"".join(chai_variety)
"  ".join(chai_variety)
"**".join(chai_variety)
```

------------------------------------------------------------------------

## Length of String

``` python
len("Masala Chai")
```

------------------------------------------------------------------------

## Looping Through String

``` python
for letter in chai:
    print(letter)
```

------------------------------------------------------------------------

## Escape Characters

``` python
chai = "He said, \"Masala chai is awesome\""
```

``` python
chai = "Masala\n chai"
```

------------------------------------------------------------------------

## Raw Strings

``` python
chai = r"Masala\nchai"
```

``` python
path = r"c:\user\pwd"
```

------------------------------------------------------------------------

## Membership Operator

``` python
"Masala" in chai
"Masalaa" in chai
```