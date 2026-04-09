from datetime import datetime

age = input("Enter you age here : ")
age_int = int(age)
day = datetime.now().strftime("%A")
day_str = str(day)


price = 12 if age_int >= 18 else 8

if day_str == "Thursday":
    price -= 2

print("Ticket prices for you is $",price)
