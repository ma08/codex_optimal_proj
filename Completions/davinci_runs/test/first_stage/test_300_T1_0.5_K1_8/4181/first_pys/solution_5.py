

from sys import stdin

def solve(N, A, B):
    A.insert(0, 0)
    A.append(0)
    B.append(0)
    S = 0
    for i in range(N+1):
        S += min(A[i]+A[i+1], B[i])
        A[i+1] = A[i+1] - min(A[i]+A[i+1], B[i])
        A[i] = A[i] - min(A[i], B[i])
    return S

def main():
    N = int(stdin.readline().strip())
    A = [int(x) for x in stdin.readline().strip().split()]
    B = [int(x) for x in stdin.readline().strip().split()]
    print(solve(N, A, B))

if __name__ == '__main__':
    main()