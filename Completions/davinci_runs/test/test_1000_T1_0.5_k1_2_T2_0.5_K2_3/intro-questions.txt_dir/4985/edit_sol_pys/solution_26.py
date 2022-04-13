

#-----main
T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    C = []
    for j in range(N):
        C.append(A[j]*B[N-j-1])

    print(sum(C))
