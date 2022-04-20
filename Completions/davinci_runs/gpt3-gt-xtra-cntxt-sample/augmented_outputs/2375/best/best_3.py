def three_block_palindrome(a):
    """
    :param a:
    :return:
    """
    n = len(a)
    f = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                f[i][j] = 1
            elif a[i] == a[j]:
                f[i][j] = 2
            else:
                f[i][j] = max(f[i + 1][j], f[i][j - 1], f[i + 1][j - 1] + 2)
    return f[0][n - 1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(three_block_palindrome(a))