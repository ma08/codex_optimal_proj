
import sys

N = int(sys.stdin.readline())

for i in range(100, N + 1):
    if len(set(list(str(i)))) == 1:
        print(i)
        break
