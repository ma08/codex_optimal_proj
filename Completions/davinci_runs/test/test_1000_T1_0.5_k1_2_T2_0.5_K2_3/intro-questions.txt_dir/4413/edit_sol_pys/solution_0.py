# cook your dish here
# cook your dish here
import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:m]
    s = set(a)
    for i in b:
        if i in s:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
