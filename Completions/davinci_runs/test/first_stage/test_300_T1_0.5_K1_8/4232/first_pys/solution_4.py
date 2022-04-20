
from bisect import bisect_left
from typing import List

from algorithms.binary_search import binary_search


def find_k_th_element(lst: List[int], k: int) -> int:
    """
    >>> find_k_th_element([3, 7, 5, 1, 10, 3, 20], 4)
    6
    >>> find_k_th_element([3, 7, 5, 1, 10, 3, 20], 2)
    -1
    """
    lst = sorted(lst)
    if k == 0:
        return -1
    elif k == len(lst):
        return lst[-1]
    else:
        return lst[k - 1]


def find_k_th_element_with_binary_search(lst: List[int], k: int) -> int:
    """
    >>> find_k_th_element_with_binary_search([3, 7, 5, 1, 10, 3, 20], 4)
    6
    >>> find_k_th_element_with_binary_search([3, 7, 5, 1, 10, 3, 20], 2)
    -1
    """
    lst = sorted(lst)
    if k == 0:
        return -1
    elif k == len(lst):
        return lst[-1]
    else:
        return binary_search(lst, k)


def find_k_th_element_with_bisect(lst: List[int], k: int) -> int:
    """
    >>> find_k_th_element_with_bisect([3, 7, 5, 1, 10, 3, 20], 4)
    6
    >>> find_k_th_element_with_bisect([3, 7, 5, 1, 10, 3, 20], 2)
    -1
    """
    lst = sorted(lst)
    if k == 0:
        return -1
    elif k == len(lst):
        return lst[-1]
    else:
        return bisect_left(lst, lst[k - 1]) + 1


if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(find_k_th_element_with_bisect(lst, k))