
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(1, N):
    if i % 2 == 0:
        ans += A[i]
print(ans)
