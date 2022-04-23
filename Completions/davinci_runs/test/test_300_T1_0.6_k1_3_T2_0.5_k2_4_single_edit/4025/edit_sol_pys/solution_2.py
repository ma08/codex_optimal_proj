
import math
n = int(input())
a = list(map(int, input().split()))

m = 0
for i in a:
    m = max(m, i)

ans = 0
for i in a:
    ans += m-i

print(ans)
