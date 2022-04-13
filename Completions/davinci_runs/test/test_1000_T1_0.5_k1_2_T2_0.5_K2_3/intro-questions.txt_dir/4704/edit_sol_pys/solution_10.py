
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(N):
    if K <= A[i]:
        print(i)
        exit()
    else:
        K -= A[i]


