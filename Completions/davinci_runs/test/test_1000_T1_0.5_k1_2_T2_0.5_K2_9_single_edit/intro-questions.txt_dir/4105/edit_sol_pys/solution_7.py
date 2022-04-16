
import sys


if not (n <= 100 and k <= 100):
    sys.exit()
n, k = [int(x) for x in input().split()]

if n == 2:
    print("YES")
    print("1 2\n2 1")
else:
    print("YES")
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
