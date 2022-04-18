
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

N, M = read_ints()
A = [0] * N
for i in range(M):
    x, y = read_ints()
    A[x-1] |= 1 << (y-1)
    A[y-1] |= 1 << (x-1)

def read_int():
    return int(sys.stdin.readline())    

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

Q = read_int()
for i in range(Q):
    x, y = read_ints()
    if A[x-1] & (1 << (y-1)):
        print("YES")
    else:
        print("NO")
