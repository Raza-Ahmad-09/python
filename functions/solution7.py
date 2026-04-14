def sum_all(*args):
    # print(*args)
    print(args) # as it returns a tuple so we can perform operations using loops
    for i in args:
        print(i * 2)
    return sum(args) # we can use sum()

print(sum_all(1,4,6,7))