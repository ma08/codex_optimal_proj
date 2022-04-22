import math


N = int(input())

ans = 0

for i in range(N):
    A = int(input()) - 1
    ans += 1
    for j in range(N):
        if j != A:
            ans -= 1

print(ans)
