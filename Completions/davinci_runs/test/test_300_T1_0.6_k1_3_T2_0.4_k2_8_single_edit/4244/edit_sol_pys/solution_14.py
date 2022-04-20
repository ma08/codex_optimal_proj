import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
# -- Calculate mean of all x coordinates
mean = sum(x) / n
# -- Store differences between mean and all x coordinates in a list
diff = [abs(mean - x[i]) for i in range(n)]
print(sum(diff))
