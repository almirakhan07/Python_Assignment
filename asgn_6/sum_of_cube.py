n = int(input("enter the last number whose sum you want:"))
sum_ = 0
for i in range(1,n+1):
    d = i**3
    sum_ = sum_ + d
print(sum_)