x = int(input("enter a number"))
factor = 0
def prime_num():
    factor = 0
    for j in range(1, x+1):
        if x % j == 0:
            factor = factor +1
            if factor > 2:
                return f"{x} is a prime number"
            else:
                return f"{x} is not a prime number"
a = prime_num()
print(a)

