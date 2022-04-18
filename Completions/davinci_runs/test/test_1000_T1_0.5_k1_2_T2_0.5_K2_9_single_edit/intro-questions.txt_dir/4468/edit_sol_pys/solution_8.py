
import sys

N, T = map(int, sys.stdin.readline().rstrip().split())  # N:個数 T:時間
t = list(map(int, sys.stdin.readline().rstrip().split()))  # t:時刻

total = 0
start = 0

for i in range(N):  # 各時刻について
    if t[i] < start:
        total += T
    else:
        total += T + t[i] - start
        start = t[i]

print(total)
