

import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

if n > 0:
    res = []
    while n > 0:
        res.append(str(n % 2))
        n //= 2
    print("".join(res[::-1]))
    exit()

# n < 0
n = abs(n)
rem = 1
res = []
while n > 0:
    if n % 2 == 0:
        res.append("1")
        n = (n // 2) + rem
    else:
        res.append("0")
        n //= 2
        rem = 1

print("1" + "".join(res[::-1]))
