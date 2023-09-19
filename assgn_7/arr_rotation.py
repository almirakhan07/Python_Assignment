arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    x = int(input("enter the element:"))
    arr.append(x)
print(arr)
def array_rotation():
    for i in range(len(arr)):
        arr.insert(i,arr[-1])
        del arr[-1]
    return arr
k = array_rotation()
print(k)