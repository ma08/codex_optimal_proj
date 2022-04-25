

N = int(input())
a = list(map(int, input().split()))

# 部分点解法
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += a[i] * a[j]
print(ans)

print(ans)
