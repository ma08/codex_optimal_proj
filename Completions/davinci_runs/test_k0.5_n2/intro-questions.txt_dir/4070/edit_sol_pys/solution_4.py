
def get_odd_divisors_of_n(n):
    """
    :param n: int
    :return: set
    """
    assert 0 <= n <= 2000000000
    if n == 0:
        return set()
    if n == 1:
        return {1}
    if n % 2 == 0:
        return get_odd_divisors_of_n(n // 2)
    else:
        return get_odd_divisors_of_n((n - 1) // 2) | {n}


def count_divisors(n):
    """
    :param n: int
    :return: int
    """
    assert 0 <= n <= 2000000000
    return len(get_odd_divisors_of_n(n))


def main():
    n = int(input())
    print(count_divisors(n))


if __name__ == '__main__':
    main()
