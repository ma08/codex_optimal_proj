
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
    if len(set(a)) == 1:  # 全て同じ数字
        return 'YES'
    if len(set(a)) == 2:  # 2種類の数字
        if a.count(max(set(a))) == 1:  # 最大の数字が1つだけ
            return 'YES'
        else:
            return 'NO'
    if len(set(a)) > 2:  # 3種類以上の数字
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
