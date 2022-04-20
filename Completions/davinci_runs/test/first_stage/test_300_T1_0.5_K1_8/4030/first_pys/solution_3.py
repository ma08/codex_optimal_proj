

#-----SOLUTION-----

import sys
input = sys.stdin.readline

n = int(input())
s = input()

ans = [1] * n
for i in range(1, n):
    if s[i] == s[i-1]:
        ans[i] = ans[i-1]
    else:
        ans[i] = ans[i-1] + 1
print(max(ans))
print(*ans)