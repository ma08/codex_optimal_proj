# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 18:50:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 18:51:15

# https://atcoder.jp/contests/abc178/tasks/abc178_c

import sys
read = sys.stdin.readline

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))

x.sort()

dist = []
for i in range(N):
    dist.append(abs(X - x[i]))
dist.sort()

ans = 0
for i in range(1, N):
    ans = max(ans, (dist[i] - dist[i - 1]) // 2)

print(ans)
