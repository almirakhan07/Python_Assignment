fib_seq=[1,1]
n = int(input("enter the size of sequence:"))
def fib_sequence():
    for i in range(2,n):
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq
a = fib_sequence()
print(a)