fruit_clr = str(input("Analyze and enter fruit color : "))

if fruit_clr in ["Green","green","GREEN"]:
    print("Fruit is Unripe")
elif fruit_clr in ["Yellow","yellow","YELLOW"]:
    print("Fruit is ripe")
elif fruit_clr in ["Brown","brown","BROWN"]:
    print("Fruit is overripe")