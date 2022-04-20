

# My Answer
import math

N = int(input())

min_count = math.inf

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        count = 0
        if i == 1:
            count += 1
        else:
            count += i - 1
        if N // i == 1:
            count += 1
        else:
            count += N // i - 1
        min_count = min(min_count, count)

print(min_count)

# Shortest Answer
"""
import math

N = int(input())

min_count = math.inf

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        count = 0
        if i == 1:
            count += 1
        else:
            count += i - 1
        if N // i == 1:
            count += 1
        else:
            count += N // i - 1
        min_count = min(min_count, count)

print(min_count)
"""