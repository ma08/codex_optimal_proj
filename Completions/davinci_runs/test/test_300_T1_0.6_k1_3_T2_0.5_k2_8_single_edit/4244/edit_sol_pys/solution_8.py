import sys

n = int(input())
x = list(map(int, input().split()))

# -- Calculate mean of all x coordinates
mean = sum(x) / float(n)

# -- Store differences between mean and all x coordinates in a list
diff = [abs(mean - x[i]) for i in range(n)]

print(sum(diff))
