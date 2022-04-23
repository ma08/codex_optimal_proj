from collections import defaultdict
from itertools import combinations
from typing import List, Tuple


def find_max_diff(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_2(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_3(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_4(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_5(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_6(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_7(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_8(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_9(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_10(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_11(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_12(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_13(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def find_max_diff_14(nums: List[int], k: int) -> int:
    nums.sort()
    max_diff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff <= k:
            max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


def solution(matrix, n, m, k):
    max_diff = 0
    for i in range(n):
        row = [matrix[i][j] for j in range(m)]
        row.sort()
        for j in range(m-1):
            diff = row[j+1] - row[j]
            if diff <= k:
                max_diff = max(max_diff, diff)
    return max_diff if max_diff > 0 else -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    k = int(input())
    print(solution(matrix, n, m, k))
