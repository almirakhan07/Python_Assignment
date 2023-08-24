import math
arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    num = int(input("enter a number:"))
    arr.append(num)
def split_arr(arr):
    halflen =int(math.floor(len(arr)/2))
    for i in range(0, halflen):
        arr.append(arr[i])
    arr = arr[halflen:]
    return arr
x = split_arr(arr)
print(x)

