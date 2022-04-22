

import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    C = list(map(int, sys.stdin.readline().rstrip().split()))
    S = [0]*M
    for i in range(M):
        S[i] = B[i]*C[i]
    for i in range(N):
        if A[i] < min(S):
            print(i)
            return
    print(-1)
    return

if __name__ == "__main__":
    main()
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()
