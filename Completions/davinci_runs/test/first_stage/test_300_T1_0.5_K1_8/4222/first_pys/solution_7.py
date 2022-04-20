

N, K = map(int, input().split())
A = [[] for i in range(K)]
for i in range(K):
    d = int(input())
    A[i] = list(map(int, input().split()))

ans = 0
for i in range(1, N+1):
    for j in range(K):
        if i in A[j]:
            break
    else:
        ans += 1

print(ans)