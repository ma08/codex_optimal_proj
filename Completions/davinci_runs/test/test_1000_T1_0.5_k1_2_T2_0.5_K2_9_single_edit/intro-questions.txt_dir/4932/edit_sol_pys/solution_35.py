import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()
    C.sort()
    i = 0
    j = 0
    k = 0
    ans = 0
    while j < N:
        while i < N and A[i] < B[j]:
            i += 1
        while k < N and C[k] <= B[j]:
            k += 1
        ans += (i * (N - k))
        j += 1
    print(ans)

main()
