import sys, math

n = int(sys.stdin.readline())

print(math.factorial(n) / (math.factorial(n - 3) * 6))
