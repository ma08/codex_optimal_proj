
import sys
input = sys.stdin.readline
 
N, X = map(int, input().split())
L = list(map(int, input().split()))
 
D = 0
ans = 1
for i in range(N):
    D += L[i]
    if D > X:
        break
    ans += 1
print(ans)
