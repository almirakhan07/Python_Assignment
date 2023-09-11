import math
mass = float(input("enter your mass(kg)"))
height = float(input("enter your height(metres)"))
bmi = mass/(height**2)
rounded_bmi = math.ceil(bmi)
print(rounded_bmi)
