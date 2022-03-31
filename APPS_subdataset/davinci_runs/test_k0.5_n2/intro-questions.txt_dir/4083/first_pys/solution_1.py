

from math import log2
from collections import Counter
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def get_min_operations(n, k, arr):
    """
    :param n:
    :param k:
    :param arr:
    :return:
    """
    def get_min_operations_from_dict(n, k, arr_dict):
        """
        :param n:
        :param k:
        :param arr_dict:
        :return:
        """
        def get_min_operations_from_dict_inner(n, k, arr_dict):
            """
            :param n:
            :param k:
            :param arr_dict:
            :return:
            """
            if k == 1:
                return 0
            if n == k:
                return min(map(lambda x: get_min_operations_from_dict_inner(n, k, {key: val - 1 for key, val in arr_dict.items()}) + 1, arr_dict.keys()))
            return min(map(lambda x: get_min_operations_from_dict_inner(n - 1, k, {key: val - 1 for key, val in arr_dict.items() if key != x}) + 1, arr_dict.keys()))

        if arr_dict[max(arr_dict.keys())] >= k:
            return 0
        return get_min_operations_from_dict_inner(n, k, arr_dict)

    def get_min_operations_from_arr(n, k, arr):
        """
        :param n:
        :param k:
        :param arr:
        :return:
        """
        def get_min_operations_from_arr_inner(n, k, arr):
            """
            :param n:
            :param k:
            :param arr:
            :return:
            """
            if k == 1:
                return 0
            if n == k:
                return min(map(lambda x: get_min_operations_from_arr_inner(n, k, [y for y in arr if y != x]) + 1, arr))
            return min(map(lambda x: get_min_operations_from_arr_inner(n - 1, k, [y for y in arr if y != x]) + 1, arr))

        if arr.count(max(arr)) >= k:
            return 0
        return get_min_operations_from_arr_inner(n, k, arr)

    if n <= 5:
        return get_min_operations_from_arr(n, k, arr)
    else:
        return get_min_operations_from_dict(n, k, Counter(arr))

def main():
    """
    :return:
    """
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(get_min_operations(n, k, arr))

if __name__ == '__main__':
    main()