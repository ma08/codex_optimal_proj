

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    C = list(map(int, sys.stdin.readline().rstrip().split()))
    prev = A[0]
    for i in range(1, N):
        if prev == A[i]:
            print("CONTINUE")
            return 0
        prev = A[i]
    prev = B[0]
    for i in range(1, N-1):
        if prev == B[i]:
            print("CONTINUE")
            return 0
        prev = B[i]
    prev = C[0]
    for i in range(1, N-2):
        if prev == C[i]:
            print("CONTINUE")
            return 0
        prev = C[i]
    print("FAILED")
    return

if __name__ == "__main__":
    main()
