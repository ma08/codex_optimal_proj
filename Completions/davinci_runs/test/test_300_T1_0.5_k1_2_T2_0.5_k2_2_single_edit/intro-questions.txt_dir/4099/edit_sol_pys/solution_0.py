N, K, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if M*N > sum(A):
    ans = M*N - sum(A)
print(ans)
