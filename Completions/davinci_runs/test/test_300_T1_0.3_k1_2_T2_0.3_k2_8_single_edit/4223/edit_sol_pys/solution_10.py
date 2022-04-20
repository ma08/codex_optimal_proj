

import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i < j:
                ans += A[i] * A[j]
    print(ans)

if __name__ == '__main__':
    main()
