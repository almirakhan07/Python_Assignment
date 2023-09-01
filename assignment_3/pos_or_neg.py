x = int(input("enter a number"))
def pos_neg():
    if x < 0:
        return x, "is a negative number"
    elif x > 0:
        return x, "is a positive number"
    else:
        return x,"is neither positive nor negative"
d = pos_neg()
print(d)