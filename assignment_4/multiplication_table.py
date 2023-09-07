def multiplication_table ():
    num = int(input("enter a number:"))
    for i in range(1, 11):
        result = num * i
        print (f"{num} x {i} ={result}")
x = multiplication_table()
print(x)
