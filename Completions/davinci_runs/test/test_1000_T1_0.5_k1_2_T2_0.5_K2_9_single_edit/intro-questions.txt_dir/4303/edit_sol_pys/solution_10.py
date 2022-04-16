
import sys

N, K = map(int, sys.stdin.readline().split())
candles = list(map(int, sys.stdin.readline().split()))
candles.sort()
min_time = 0

if K == N:
    min_time = abs(candles[-1])
elif K == 1:
    min_time = abs(candles[0])
else:
    min_time = abs(candles[K-1])
    for i in range(K-1, -1, -1):
        min_time += candles[i] * 2

print(min_time)
