

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# お菓子を箱ごとに分ける
box = [0 for i in range(N)]

# お菓子を箱ごとに入れる
for i in range(M):
    a = int(input())
    box[a - 1] += 1

# 箱ごとに出力
for i in range(N):
    print(box[i])
