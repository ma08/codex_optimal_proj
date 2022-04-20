

import sys

n = int(input())
s = [input() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if s[i][0] != s[j][0] and s[j][0] != s[k][0] and s[k][0] != s[i][0] and \
                    s[i][0] in 'MARCH' and s[j][0] in 'MARCH' and s[k][0] in 'MARCH':
                ans += 1
print(ans)