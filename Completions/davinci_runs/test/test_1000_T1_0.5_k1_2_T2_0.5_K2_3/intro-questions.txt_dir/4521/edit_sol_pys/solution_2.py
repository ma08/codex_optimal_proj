
# SOLUTION
import math

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

if k == 0:
    print(sum(a))
    exit()

a = sorted(a)
for i in range(1, len(a)):
    a[i] = min(a[i], a[i - 1] + k)

print(sum(a))
