"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

    You will pick exactly 2 numbers.
    You cannot pick the same element twice.
    If you have muliple pairs, select the pair with the largest number.
"""


def get_indices(nums, target):
    hm = {}
    result = []
    for i in range(len(nums)):
        if target - 30 - nums[i] in hm:
            result.append([i, hm[target - 30 - nums[i]]])
        hm[nums[i]] = i

    if not result:
        return []

    result = sorted(result, key=lambda x: x[0])
    return result[-1]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    print(get_indices(nums, target))
