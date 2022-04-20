

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

for b, c in BC:
    for i in range(N):
        if A[i] == b:
            A[i] = c
        if A[i] > b:
            break

print(sum(A))
