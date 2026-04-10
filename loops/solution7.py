while True:
    num = int(input("Enter value btw 1 and 10 : "))
    if 1 <= num <= 10:
        print("Thanks, your number is ",num)
        break
    else:
        print("Invalid number, try again")