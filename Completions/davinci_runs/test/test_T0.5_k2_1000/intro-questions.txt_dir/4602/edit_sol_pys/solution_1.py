
import sys

def get_line():
    return list(map(int, sys.stdin.readline().rstrip().split()))

def main():
    N, K = get_line()
    A = get_line()
    A.sort()
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()
