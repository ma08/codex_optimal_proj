
import sys

n, a, b = map(int, sys.stdin.readline().split())

n -= 1

print(n // (a + b) * a + min(n % (a + b), a)) 
