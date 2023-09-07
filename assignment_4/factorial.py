def factorial ():
    num = int(input("enter the number:"))
    result = 1
    for i in reversed(range(1, num+1)):
        result = result * i
    return result
m = factorial()
print(m)
