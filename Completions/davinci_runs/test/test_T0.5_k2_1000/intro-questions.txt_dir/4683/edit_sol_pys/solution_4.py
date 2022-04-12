n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        ans += l[i] * l[j]

print(ans % (10**9+7))
