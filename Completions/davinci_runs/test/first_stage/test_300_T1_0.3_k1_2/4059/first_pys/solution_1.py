

import math

N = int(input())

count = 0
for a in range(1, int(math.sqrt(N))+1):
    for b in range(1, N):
        if a*b+b > N:
            break
        if a*b+b == N:
            count += 1

print(count)