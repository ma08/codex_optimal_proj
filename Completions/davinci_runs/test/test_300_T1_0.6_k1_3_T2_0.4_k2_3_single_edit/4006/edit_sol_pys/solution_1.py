
import sys

n = int(sys.stdin.readline())

def solve(n):
    count = 0
    while n % 10 == 0:
        n //= 10
        count += 1
    return n + 1, count

while n != 1:
    n, count = solve(n)
    print(count)
