
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for i in range(1, N, 2):
    ans += A[i]
print(ans)
