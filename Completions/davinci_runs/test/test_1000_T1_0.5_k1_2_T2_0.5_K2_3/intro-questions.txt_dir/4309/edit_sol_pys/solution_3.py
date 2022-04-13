import sys

N = int(sys.stdin.readline())

for i in range(N + 1, 10000):
    if len(set(list(str(i)))) == 1 and len(list(str(i))) == 4:
        print(i)
        break
