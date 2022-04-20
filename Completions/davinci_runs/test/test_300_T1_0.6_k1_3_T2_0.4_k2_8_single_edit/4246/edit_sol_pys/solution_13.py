
N = int(input())
A = list(map(int, input().split()))
ans = 10 ** 9
for i in range(N):
    ans = min(ans, abs(A[i] - A[i + 1]))
print(ans)
