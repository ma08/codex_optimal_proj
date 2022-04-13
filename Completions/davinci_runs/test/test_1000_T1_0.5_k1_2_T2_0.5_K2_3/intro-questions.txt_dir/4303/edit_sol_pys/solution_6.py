
import sys

N, K = map(int, sys.stdin.readline().split())
candles = list(map(int, sys.stdin.readline().split()))  # 유지할 수 있는 촛불의 수

# print(N, K)
# print(candles)

candles.sort()  # 촛불의 길이를 오름차순 정렬

# print(candles)

min_time = 0

if K == N:
    min_time = abs(candles[-1])
elif K == 1:
    min_time = abs(candles[0])
else:
    min_time = abs(candles[K - 1])
    for i in range(K - 1, -1, -1):
        min_time += candles[i] * 2

print(min_time)
