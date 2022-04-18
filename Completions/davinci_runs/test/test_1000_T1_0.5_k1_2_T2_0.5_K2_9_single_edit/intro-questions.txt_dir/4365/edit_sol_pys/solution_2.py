

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # See:
    # https://beta.atcoder.jp/contests/abc067/submissions/1795663
    total = sum(A)
    target = total / (4 * M)
    count = 0
    for a in A:
        if a >= target:
            count += 1

    if count >= M:
        print('Yes')
    else:
        print('No')
