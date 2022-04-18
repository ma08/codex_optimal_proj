

def main():
    """AOJ question ALDS1_1_B

    N = 2

    >>> main()
    2
    1 4
    5
    >>> main()
    5
    -37 -3 -13 4 -21
    556
    >>> main()
    3
    -2 3 -4
    4
    X = [1,4]
    """
    N = int(input())
    X = [int(x) for x in input().split()]

    # Xの中央値が最小となる
    X.sort()
    # print(X)
    if N % 2 == 0:
        # 偶数
        median = (X[N//2-1] + X[N//2]) / 2
    else:
        # 奇数
        median = X[N//2]

    # print(median)
    ans = 0
    for x in X:
        ans += (x - median)**2
    print(ans)


if __name__ == '__main__':
    main()
