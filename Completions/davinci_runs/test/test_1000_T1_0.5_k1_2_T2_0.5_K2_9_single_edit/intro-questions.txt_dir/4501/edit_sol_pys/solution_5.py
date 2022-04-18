
import itertools
import math

N, A = map(int, input().split())
X = list(map(int, input().split()))

n, a = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    for j in itertools.combinations(x, i):
        if sum(j) / i == a:
            ans += 1
print(ans)
