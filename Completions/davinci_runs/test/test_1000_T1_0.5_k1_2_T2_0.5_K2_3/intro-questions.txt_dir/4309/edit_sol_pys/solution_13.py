
import sys

N = int(sys.stdin.readline())

for n in range(100, N + 1):
    if len(set(list(str(n)))) == 1:
        print(n)
        break
