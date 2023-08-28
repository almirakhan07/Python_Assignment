def swap_var ():
    a = int(input("enter a numerical value for a:"))
    b = int(input(("enter a numerical value for b:")))
    c = a
    a = b
    b = c
    return "a is now " + str(a)+" b is now "+str(b)
l = swap_var()
print(l)