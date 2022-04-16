

n = int(input())
num = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        ans += num[i] * num[j]

print(ans)
