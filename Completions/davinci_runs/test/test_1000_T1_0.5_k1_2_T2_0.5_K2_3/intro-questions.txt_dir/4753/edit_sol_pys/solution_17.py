
import sys
import math

n = int(sys.stdin.readline())

print(math.factorial(n) / (math.factorial(n - 3) * 6))
