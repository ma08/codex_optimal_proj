
N = int(input())
A = list(map(int, input().split()))

ans = 1
m = A[0]
for i in range(1, N):
    if m >= A[i]:
        ans += 1
        m = A[i]

print(ans)
