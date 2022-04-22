


# 그냥 문제를 잘 읽어야한다.
# 반복문을 돌리면서 하나씩 더해나가고 최종값이 x보다 작은지 비교하면 된다.
import sys

n, x = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

d = 0
cnt = 0

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
