
n = int(input())
h = list(map(int, input().split()))

ans = h[0]
for i in range(n):
    if h[i] > ans:
        ans = h[i]

print(ans)
