arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    num = int(input("enter a number:"))
    arr.append(num)
def largest_num():
    b = 0
    for i in range(len(arr)):
        if arr[i] > b:
            b = arr[i]
    return b
d = "largest number in your array is "+str(largest_num())
print(d)



