
N = int(input())
A = list(map(int, input().split()))

ans = 1
for i in range(1, N):
    if A[i] > A[i - 1]:
        ans += 1

print(ans)
