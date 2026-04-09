age = input("Enter age here :  ");

age_int = int(age)

if age_int < 13:
    print("A Child is here")
elif age_int < 20:
    print("Teenager is here")
elif age_int < 59:
    print("Adult is here")
elif age_int > 60:
    print("Senior person is here")
