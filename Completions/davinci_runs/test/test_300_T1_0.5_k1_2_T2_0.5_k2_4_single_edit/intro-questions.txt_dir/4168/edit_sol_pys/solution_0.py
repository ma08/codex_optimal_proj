
import math
import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

n = abs(n)  # n < 0
res = []
while n > 0:
    if n % 2 == 0:
        res.append("1")
        n = (n // 2) + 1
    else:
        res.append("0")
        n //= 2

print("1" + "".join(res[::-1]))
