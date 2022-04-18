import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

N = read_int()
M = [0] * N
for i in range(N):
    M[i] = read_ints()

a = [0] * N
for i in range(N):
    for j in range(i+1, N):
        a[i] |= M[i][j]
        a[j] |= M[i][j]

print(" ".join(map(str, a)))
