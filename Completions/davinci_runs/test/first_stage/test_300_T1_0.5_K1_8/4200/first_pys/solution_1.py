

import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

if max(a) >= math.ceil(sum(a) / (4 * m)):
    print("Yes")
else:
    print("No")