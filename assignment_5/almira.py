Arr = []
n = int(input("enter the number of elements you want in your array:"))
for _ in range(n):
    num = int(input("enter a number:"))
    Arr.append(num)
def addition_of_arr (Arr):
    total = 0
    for i in Arr:
        total += i
    return total
a = "The sum of elements of your array is "+str(addition_of_arr(Arr))
print(a)
