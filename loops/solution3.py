number = 3

for i in range(1, 11):
    if i == 5:
        continue  # here the keyword continue will continue the process for provided condition, will not do any calculations
    print(number, 'x', i, '=', number * i)
