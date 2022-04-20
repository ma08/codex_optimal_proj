

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(K, N):
    ans += A[i] - A[i - K]



# N, K = list(map(int, input().split()))
# A = list(map(int, input().split()))

# A.sort()

# ans = 0
# for i in range(K, N):
#     ans += A[i] - A[i - K]

# print(ans)

print(ans)
