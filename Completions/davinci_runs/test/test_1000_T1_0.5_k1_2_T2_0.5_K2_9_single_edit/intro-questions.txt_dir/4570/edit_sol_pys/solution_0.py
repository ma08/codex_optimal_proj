
#A

N, A, B = map(int, input().split())

#B
N, K = map(int, input().split())
print(N%K)
print(min(A*N, B))
