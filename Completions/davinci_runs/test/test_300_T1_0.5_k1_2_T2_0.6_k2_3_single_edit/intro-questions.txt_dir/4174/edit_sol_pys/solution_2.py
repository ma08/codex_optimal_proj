import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))  # x가 담길 list

d = 0  # 거리
cnt = 0  # 지나간 돌들의 개수

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
