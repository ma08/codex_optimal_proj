
def solver(n, a):
    """
    >>> solver(5, [2, 1, 1, 2, 5])
    'YES'
    >>> solver(3, [4, 5, 3])
    'YES'
    >>> solver(2, [10, 10])
    'YES'
    >>> solver(3, [1, 2, 3])
    'NO'
    """
    if len(set(a)) == 1:  # 全部同じ値だった場合
        return 'YES'
    if len(set(a)) == 2:  # 2種類の値がある場合
        if a.count(max(set(a))) == 1:  # 最大値が1つだけだった場合
            return 'YES'
        else:
            return 'NO'
    if len(set(a)) > 2:  # 3種類以上の値がある場合
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
