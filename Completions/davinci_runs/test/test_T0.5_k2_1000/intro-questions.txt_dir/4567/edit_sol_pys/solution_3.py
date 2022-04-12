import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    A.sort(reverse=True)
    print(A[0] + A[1] + A[2])

if __name__ == '__main__':
    main()
