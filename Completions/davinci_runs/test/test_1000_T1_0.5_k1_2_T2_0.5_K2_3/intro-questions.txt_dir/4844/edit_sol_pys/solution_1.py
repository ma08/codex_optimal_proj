import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

N = read_int()
M = [0] * N
for i in range(N):
    M[i] = read_ints()

a = [0] * N
for i in range(N):
    for j in range(N):
        a[i] |= M[i][j] | M[j][i]

print(" ".join([str(x) for x in a]))
