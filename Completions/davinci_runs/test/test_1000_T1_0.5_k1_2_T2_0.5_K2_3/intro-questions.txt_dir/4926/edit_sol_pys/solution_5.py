
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(sys.stdin.readline())

print(sum([1/factorial(x) for x in range(n)]))
