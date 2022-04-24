

import sys

def print_ans(n, ans):
    """Test Case
    >>> print_ans(3, [2, 3, 4])
    2 3 4 
    >>> print_ans(2, [1, 2])
    1 2
    """
    for i in range(n):
        print(ans[i])


def solver(n, a):
    """Test Case
    >>> solver(3, [1, 2, 3])
    [2, 3, 4]
    >>> solver(4, [4, 3, 2, 1])
    [5, 4, 3, 2]
    """
    ans = [None] * n
    for i in range(n):
        ans[i] = a[i] + 1
    return ans

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ans = solver(n, a)
    print_ans(n, ans)

    # # test
    # import doctest
    # doctest.testmod()
    # #unittest.main()
