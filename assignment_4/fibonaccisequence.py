def fib_seq ():
    num = int(input("enter number of terms you want in your sequence"))
    seq = [0, 1]
    for i in range(2, num):
        seq.append(seq[-1] + seq[-2])
    return f"fibonacci sequence pto {num} is {seq}"
d = fib_seq()
print(d)