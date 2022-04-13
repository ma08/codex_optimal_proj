import sys

N, T = map(int, sys.stdin.readline().rstrip().split())
t = list(map(int, sys.stdin.readline().rstrip().split()))
total = 0
start = 0
# 마지막 지점에서 대기 시간이 필요하지 않으므로 마지막 지점은 제외
for i in range(N):
    if t[i] < start:
        total += T
    else:
        total += T + t[i] - start
        start = t[i]
print(total)
