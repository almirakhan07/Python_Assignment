
def arms_number (number):
    n_str = str(number)
    digits = len(n_str)
    sum_ = 0
    for i in (n_str):
        d = int(i)
        sum_ += d**digits
    return sum_ == number
range_start = int(input("enter the beginning of interval"))
range_end = int(input("enter the end of interval"))
def armstrong_num_in_range(range_start, range_end):
    for i in range(range_start, range_end):
        if i == arms_number():
            print(i, end=" ")

