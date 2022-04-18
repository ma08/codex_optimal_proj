
import sys
from math import log
from bisect import bisect_left
 
def is_power_of_3(x):
    return x > 0 and 3 ** round(log(x, 3)) == x
 
# If a number is a power of 3, then the next power of 3 is the next good number
good_numbers = [3 ** i for i in range(1, int(log(10 ** 18, 3)))]
 
q = int(input())
for _ in range(q):
    n = int(input())
    print(good_numbers[bisect_left(good_numbers, n)])
