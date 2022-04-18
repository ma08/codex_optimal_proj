
#this is a comment
import math

def calculate(n):
    if n == 1:
        return 0

    if n % 2 == 0 and n != 2:
        return 1 + calculate(n/2)
    if n % 3 == 0 and n != 3:
        return 1 + calculate(2*n/3)
    if n % 5 == 0 and n != 5:
        return 1 + calculate(4*n/5)
    return -1

q = int(input())

for i in range(q):
    n = int(input())
    print(calculate(n))
