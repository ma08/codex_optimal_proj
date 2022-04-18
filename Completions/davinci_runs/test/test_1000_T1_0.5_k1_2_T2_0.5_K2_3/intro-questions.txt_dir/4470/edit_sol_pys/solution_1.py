
#this is a comment
import math

def calculate(num):
    if num == 1:
        return 0

    if num % 2 == 0:
        return 1 + calculate(num/2)
    if num % 3 == 0:
        return 1 + calculate(2*num/3)
    if num % 5 == 0:
        return 1 + calculate(4*num/5)
    return -1

q = int(input())

for i in range(q):
    n = int(input())
    print(calculate(n))
