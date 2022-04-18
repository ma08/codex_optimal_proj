import sys

# -- Read in number of x coordinates
n = int(sys.stdin.readline())

# -- Read in x coordinates
x = list(map(int, sys.stdin.readline().split()))

# -- Calculate mean of all x coordinates
mean = sum(x) / n

# -- Store differences between mean and all x coordinates in a list
diff = [abs(mean - x[i]) for i in range(n)]

# -- Print sum of differences
print(sum(diff))
