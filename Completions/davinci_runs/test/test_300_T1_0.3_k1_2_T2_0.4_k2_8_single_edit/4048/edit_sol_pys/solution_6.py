
import sys

n = int(sys.stdin.readline())

result = 0
while n > 0:
    if n % 2 == 0:
        n = n // 2
    else:
        n -= 1
    result += 1

print(result)
