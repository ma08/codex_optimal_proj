import math


def get_num(k):
    num_digits = math.ceil(math.log10(k))
    num_index = (k - 10**(num_digits - 1)) // num_digits
    num = 10**(num_digits - 1) + num_index
    return num

q = int(input())
for i in range(q):
    k = int(input())
    print(get_num(k))
