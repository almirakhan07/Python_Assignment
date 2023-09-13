def fib_seq(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_seq(n - 1) + fib_seq(n - 2)

# Input the number of terms you want in the Fibonacci sequence
n = int(input("Enter the sixe of sequence: "))

for i in range(n):
        print(fib_seq(i), end = " ")
