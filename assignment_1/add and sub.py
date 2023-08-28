def ap_opt():
    x = int(input("enter a number"))
    y = int(input("enter another number"))
    op = (input("enter operator"))
    if op == "+":
        return x + y
    elif op == "-":
        return x-y
    elif op == "*":
        return x * y
    elif op == "/":
        return x/y
    else:
        return "error"
l = ap_opt()
print(l)
