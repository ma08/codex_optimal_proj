


def solve(n, a):
    """
    Find the number of pairs of indices (l, r) (1 <= l <= r <= n) such that the value of median of a_l, a_{l+1}, ..., a_r is exactly the given number m.

    :param n: length of the given sequence (1 <= n <= 200000)
    :param a: sorted array of integers (1 <= a_i <= 200000)
    :return: the required number
    """
    pass


def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    print(solve(n, a))


if __name__ == "__main__":
    main()
