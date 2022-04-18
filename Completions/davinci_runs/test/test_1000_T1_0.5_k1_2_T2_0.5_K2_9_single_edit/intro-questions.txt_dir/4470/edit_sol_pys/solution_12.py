# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def calculate(n, steps = 0):
    if n == 1:
        return steps

    if n % 2 == 0:
        return calculate(n/2, steps + 1)
    if n % 3 == 0:
        return calculate(2*n/3, steps + 1)
    if n % 5 == 0:
        return calculate(4*n/5, steps + 1)
    return -1

q = int(input())

for i in range(q):
    n = int(input())
    print(calculate(n))
