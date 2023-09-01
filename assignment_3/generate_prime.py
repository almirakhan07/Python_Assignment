def prime_generator ():
    range_start = int(input("enter the beginning of your range:"))
    range_end = int(input("enter the end of your range:"))
    #factor = 0
    for i in range(range_start, range_end+1):
        factor = 0
        for j in range (1, i+1):
            if i % j == 0:
                factor = factor + 1
        if factor == 2:
            print( i, end=' ')
a = prime_generator()
print(a)
