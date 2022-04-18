

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if N < M:
    print("NO")
else:
    A.sort()
    B.sort()

    for i in range(M):
        if A[i] < B[i]:
            print("NO")
            exit()
    print("YES")
