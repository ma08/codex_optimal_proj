
from collections import defaultdict
from queue import Queue

n, d, k = map(int, input().split())

if d == 1:
    if n == 2:
        print("YES")
        print(1, 2)
    else:
        print("NO")
elif d == 2:
    if n <= k + 1:
        print("YES")
        for i in range(2, n + 1):
            print(1, i)
    else:
        print("NO")
elif d == 3:
    if n <= 2 * k + 1:
        print("YES")
        for i in range(2, n + 1):
            print(1, i)
    else:
        print("NO")
else:
    if n <= 3 * k + 1:
        print("YES")
        for i in range(2, n + 1):
            print(1, i)
    else:
        print("NO")