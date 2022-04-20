

import math

a, b, c, d = map(int, input().split())

if(a <= c):
    ans = max(b * d, a * d, b * c)
else:
    ans = max(b * d, a * d, b * c, a * c)

print(ans)