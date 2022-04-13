import sys

N = int(sys.stdin.readline())

cnt = 0

for i in range(1, N + 1):
    cnt += 1
    if cnt % 10 == 0:
        print(i, end='\n')
    else:
        print(i, end=' ')
