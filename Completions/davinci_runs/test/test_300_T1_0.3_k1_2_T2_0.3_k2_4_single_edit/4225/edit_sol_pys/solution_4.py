
import sys

a, b, c, k = map(int, sys.stdin.readline().split())  # read the input

if k <= a:  # if k is less than or equal to a
    print(k)
elif k <= a + b:  # if k is less than or equal to a + b
    print(a)
else:  # if k is greater than a + b
    print(a - (k - a - b))
