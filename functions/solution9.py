def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i #the key word yield not only return the result but also keep the function and its state in memory.



for num in even_generator(10):
    print(num)