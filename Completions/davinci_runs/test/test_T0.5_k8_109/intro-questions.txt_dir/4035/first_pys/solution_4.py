

import math

A, B = map(int, input().split())

for i in range(1, 101):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        exit()
print(-1)