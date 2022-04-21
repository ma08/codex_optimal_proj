
import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)

else:
    res = []
    while n > 0:
        res.append(str(n % 2))
        n //= 2
    print("".join(res[::-1]))
