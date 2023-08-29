import math
def quadratic_equation (a, b, c):
    discriminant =(b ** 2)-4*a*c
    if discriminant > 0:
        root_1 = (-b + math.sqrt(discriminant)) / 2*a
        root_2 = (-b - math.sqrt(discriminant)) / 2*a
        return root_1 , root_2
    elif discriminant == 0:
        root = -b / 2*a
        return root
    else :
        return "no real roots"
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))
if a == 0:
    print("a cannot equal to 0")
else:
    x = quadratic_equation(a, b, c)
    print(x)