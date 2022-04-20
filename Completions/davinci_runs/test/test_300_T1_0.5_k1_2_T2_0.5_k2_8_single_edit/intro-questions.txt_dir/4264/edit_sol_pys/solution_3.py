

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(M):
    B, C = map(int, input().split())
    for j in range(B):
        A.append(C)
    A.sort(reverse=True)
    print(A)
