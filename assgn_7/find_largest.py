arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    x = int(input("enter the element:"))
    arr.append(x)
print(arr)
def find_largest():
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return f"The largest number from the above array is {largest}"
l = find_largest()
print(l)
