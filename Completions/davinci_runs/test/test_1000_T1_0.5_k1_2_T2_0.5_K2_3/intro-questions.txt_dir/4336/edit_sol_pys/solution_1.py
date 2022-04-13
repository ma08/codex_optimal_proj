# https://atcoder.jp/contests/abc102/tasks/abc102_b

import math

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        ans += A[i]-1
    # output
    print(ans)

if __name__ == '__main__':
    main()
