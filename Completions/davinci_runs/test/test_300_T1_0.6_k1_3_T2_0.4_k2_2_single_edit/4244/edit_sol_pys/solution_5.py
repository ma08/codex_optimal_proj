import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# -- Calculate mean of all a coordinates
mean = sum(a) / n

# -- Store differences between mean and all a coordinates in a list
diff = [abs(mean - a[i]) for i in range(n)]

print(sum(diff))
