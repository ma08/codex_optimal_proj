
n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(n):
    if h[i] > ans:
        ans = h[i]
print(ans)
