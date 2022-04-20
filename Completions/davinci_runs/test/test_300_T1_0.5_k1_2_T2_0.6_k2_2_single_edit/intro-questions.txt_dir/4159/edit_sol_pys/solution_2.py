

N,M = map(int, input().split())
A = list(map(int, input().split()))

# A.sort()
# A.reverse()

# ans = 0
# for i in range(M):
#     ans += A[i]
# print(ans)

ans = 0
for i in range(M):
    ans += A[i]
print(ans)
