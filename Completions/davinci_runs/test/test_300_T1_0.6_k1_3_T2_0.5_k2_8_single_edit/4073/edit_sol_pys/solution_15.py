# Read input
n = int(input())
a = list(map(int, input().split()))[:n]

# Compute and print answer
print(sum(a) - n)
