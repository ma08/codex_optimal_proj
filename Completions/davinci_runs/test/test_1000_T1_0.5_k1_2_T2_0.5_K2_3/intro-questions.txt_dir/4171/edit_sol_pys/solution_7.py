

# Solution

n = int(input())
a = list(map(int, input().split()))[:n]

print(max(a) - min(a) + 1)
