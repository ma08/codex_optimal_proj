

import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i]
    print(ans)


if __name__ == '__main__':
    main()
