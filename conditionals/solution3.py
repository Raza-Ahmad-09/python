score = int(input("Enter your score : "))

if score >= 101:
    print("Please check your score again. Thank You")
    exit()

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score < 60:
    print("Beta gher jao")