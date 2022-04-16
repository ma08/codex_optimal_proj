

import math
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    for i in range(len(a)):
        if a[i] == a[i + 1]:
            print(a[i], a[i + 1])
            break
