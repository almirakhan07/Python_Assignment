number = int(input("enter a number:"))
n_str = str(number)
digits = len(n_str)
sum_ = 0
for i in (n_str):
    d = int(i)
    sum_ += d**digits

if sum_ == number:
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong number")


