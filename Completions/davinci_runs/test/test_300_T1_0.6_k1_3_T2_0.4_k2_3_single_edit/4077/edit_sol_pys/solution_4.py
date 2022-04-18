def solve(n, m, a):
    """
    Find the number of pairs of indices (l, r) (1 <= l <= r <= n) such that the value of median of a_l, a_{l+1}, ..., a_r is exactly the given number m.

    :param n: length of the given sequence (1 <= n <= 200000)
    :param m: required value of the median (1 <= m <= 200000)
    :param a: sorted array of integers (1 <= a_i <= 200000)
    :return: the required number
    """
    # O(n)
    left = 0
    right = 0
    cnt = 0

    while right < n:
        while right < n and a[right] == m:
            right += 1
            cnt += right - left

        while left < right and a[left] == m:
            left += 1
            cnt -= right - left

        if right >= n or a[right] < m:
            right += 1
        else:
            left += 1

    return cnt


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    assert len(a) == n

    print(solve(n, m, sorted(a)))


if __name__ == "__main__":
    main()
