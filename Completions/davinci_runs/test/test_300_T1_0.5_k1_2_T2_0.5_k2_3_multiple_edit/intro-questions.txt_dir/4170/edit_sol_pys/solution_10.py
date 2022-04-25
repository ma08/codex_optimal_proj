import math

a, b, h, m = map(int, input().split())
h_angle = (h + m / 60) * 360 / 12
m_angle = m * 360 / 60

ans = 0
curr = 0
for i in range(N-1):
    if H[i+1] <= H[i]:
        curr += 1
    else:
        ans = max(ans, curr)
        curr = 0
print(max(ans, curr))
