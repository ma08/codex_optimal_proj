

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
from itertools import accumulate
# Problem B

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # See:
    # https://beta.atcoder.jp/contests/abc067/submissions/2859138
    # https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
    # https://docs.python.org/ja/3/library/functions.html#enumerate
    acc = [0] + list(accumulate(A))
    result = 0
    for i in range(N - K + 1):
        result += acc[i + K] - acc[i]

    print(result / (N - K + 1))
