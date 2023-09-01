num = int(input("Enter a number: "))
def even_or_odd():
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
a = even_or_odd()
print(a)

