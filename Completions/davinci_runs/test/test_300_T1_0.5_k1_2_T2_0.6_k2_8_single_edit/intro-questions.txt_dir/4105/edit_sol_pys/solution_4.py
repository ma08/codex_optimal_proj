
import math

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

print(
    sum([
        abs(a[i] - b[i])
        for i in range(n)
    ])
)
