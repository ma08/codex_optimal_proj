

import sys

n, m = map(int, sys.stdin.readline().split())
s_c = [map(int, sys.stdin.readline().split()) for _ in range(m)]

if n == 1:
    if m == 1 and s_c[0][0] == 1 and s_c[0][1] == 0:
        print(0)
    else:
        print(-1)
else:
    if m == 0:
        print(10 ** (n - 1))
    else:
        ans = [0] * n
        for i in range(m):
            ans[s_c[i][0] - 1] = s_c[i][1]
        if ans[0] == 0:
            print(-1)
        else:
            print("".join(map(str, ans)))