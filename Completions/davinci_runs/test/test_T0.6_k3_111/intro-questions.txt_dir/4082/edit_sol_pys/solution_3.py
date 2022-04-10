

n = int(input())
a = list(map(int, input().split()))
# n = 5
# a = [1, 2, 5, 3, 4]
# n = 2
# a = [1, 2]
# n = 7
# a = [6, 5, 4, 3, 2, 4, 3]
# n = 5
# a = [1, 2, 3, 4, 5]
# n = 5
# a = [1, 2, 1, 2, 1]
# n = 8
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 8
# a = [8, 7, 6, 5, 4, 3, 2, 1]
# n = 8
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 7
# a = [1, 2, 3, 4, 5, 6, 7]
# n = 7
# a = [7, 6, 5, 4, 3, 2, 1]
# n = 7
# a = [1, 1, 1, 1, 1, 1, 1]


def max_increasing_subsequence(a):
    """
    :param a: list
    :return: int
    """
    n = len(a)
    if n == 1:
        return 1
    else:
        max_len = 1
        for i in range(1, n):
            if a[i] > a[i - 1]:
                max_len += 1
            else:
                break
        return max_len


def max_length_of_increasing_subarray(a):
    """
    :param a: list
    :return: int
    """
    n = len(a)
    ans = max_increasing_subsequence(a)
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            ans = max(ans, max_increasing_subsequence(a[:i] + a[i + 1:]))
    ans = max(ans, max_increasing_subsequence(a[1:]))
    return ans


print(max_length_of_increasing_subarray(a))
