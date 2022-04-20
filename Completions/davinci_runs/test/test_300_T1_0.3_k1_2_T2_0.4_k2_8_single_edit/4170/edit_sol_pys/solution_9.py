

n = int(input())
h = list(map(int, input().split()))
ans = 0

for i in range(1, n):
    if h[i - 1] >= h[i]:
        ans += 1
    else:
        h[i] = h[i - 1]

print(ans)
