

import sys

N, A, B = map(int, sys.stdin.readline().split())

# N = 8
# A = 3
# B = 4

# N = 100
# A = 0
# B = 1

count = 0
for i in range(1, N + 1):
    if i % (A + B) <= A:
        count += 1

print(count)