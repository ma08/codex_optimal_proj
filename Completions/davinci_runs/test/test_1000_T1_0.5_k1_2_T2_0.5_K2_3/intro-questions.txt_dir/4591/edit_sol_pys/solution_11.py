
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    A.sort()
    if N % 2 == 0:
        print(A[N//2-1])
    else:
        print(A[N//2])

if __name__ == "__main__":
    main()
