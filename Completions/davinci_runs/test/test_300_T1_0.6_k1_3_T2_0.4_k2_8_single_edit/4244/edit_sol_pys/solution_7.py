import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

# -- Calculate mean of all x coordinates and store it in a variable
mean = sum(x) / float(n)

# -- Store differences between mean and all x coordinates in a list called diff
diff = [abs(mean - x[i]) for i in range(n)]

# -- Print the sum of all elements in diff
print(sum(diff))
