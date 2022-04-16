
import sys
from math import log
from bisect import bisect_left

def is_power_of_2(x):
    return x > 0 and 2 ** round(log(x, 2)) == x

# If a number is a power of 2, then the next power of 2 is the next good number
good_numbers = [2 ** i for i in range(1, int(log(10 ** 18, 2)))]

q = int(input())
for _ in range(q):
    n = int(input())
    print(good_numbers[bisect_left(good_numbers, n)])
