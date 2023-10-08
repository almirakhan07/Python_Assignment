arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    num = int(input("enter a number:"))
    arr.append(num)
print(arr)
def monotonic_or_not ():
    b = arr.copy()
    b.sort()
    c = b[::-1]
    if arr == b or arr == c:
        x = "monotonic"
    else:
        x = "not monotonic"
    return x
d = "your array is "+monotonic_or_not()
print(d)