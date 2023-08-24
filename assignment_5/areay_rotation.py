arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    num = int(input("enter a number:"))
    arr.append(num)
def arr_rotation(arr):
    for i in range(len(arr)):
        arr.insert(i,arr[-1])
        del arr[-1]

    return arr
d = arr_rotation(arr)
print(d)