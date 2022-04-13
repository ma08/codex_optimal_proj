# Problem: https://atcoder.jp/contests/abc120/tasks/abc120_b

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    # print(N, K, x)
    x.sort()
    # print(x)
    print(x[K-1] - x[0])
    # min(|x_k-x_1|, |x_N-x_k|) + x_N - x_1
    print(min(abs(x[K-1] - x[0]), abs(x[-1] - x[K-1])) + x[-1] - x[0])

if __name__ == "__main__":
    main()
