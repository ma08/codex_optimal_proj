import math

n = int(input())

ans = 0
for a in range(1, int(math.sqrt(n)) + 1):
    b = n // a
    if a * b == n:
        ans += b
        if a != b:
            ans += a

print(ans)
