

N = int(input())
A = list(map(int, input().split()))
def get_distance(A, i):
    return abs(A[i] - A[i-1]) + abs(A[i] - A[(i+1)%N]) + abs(A[(i+1)%N] - A[i-1])


for i in range(N):
    print(get_distance(A, i))
