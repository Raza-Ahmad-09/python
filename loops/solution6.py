number = int(input("Enter number to find factorial : "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number -1
print(factorial)