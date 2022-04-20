import math


# Read input
n = int(input())
a = list(map(int, input().split()))

# Compute and print answer
print(math.ceil(sum(a) / n))
