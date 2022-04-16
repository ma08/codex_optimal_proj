import math


t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if math.sum(a) % 2 == 0:
        print("NO")
    else:
        print("YES")
