

#
#
# def median(nums):
#     """
#     >>> median([1,2,3,4,5])
#     3
#     >>> median([1,2,3,4])
#     2
#     >>> median([1,2,3])
#     2
#     >>> median([1,2])
#     1
#     >>> median([1])
#     1
#     """
#     sorted_nums = sorted(nums)
#     length = len(sorted_nums)
#     if length % 2:
#         return sorted_nums[length // 2]
#     else:
#         return sorted_nums[length // 2 - 1]
#
#
# def count_median_pairs(nums, median):
#     """
#     >>> count_median_pairs([2, 4, 5, 3, 1], 4)
#     4
#     >>> count_median_pairs([1, 2, 3, 4, 5], 5)
#     1
#     >>> count_median_pairs([1, 15, 2, 14, 3, 13, 4, 8, 12, 5, 11, 6, 10, 7, 9], 8)
#     48
#     """
#     count = 0
#     nums_length = len(nums)
#     for i in range(nums_length):
#         for j in range(i, nums_length):
#             if median(nums[i:j + 1]) == median:
#                 count += 1
#     return count
#
#
# def main():
#     n, m = map(int, input().split())
#     nums = list(map(int, input().split()))
#     print(count_median_pairs(nums, m))
#
#
# if __name__ == '__main__':
#     main()


def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    nums_length = len(nums)
    for i in range(nums_length):
        for j in range(i, nums_length):
            if sorted(nums[i:j + 1])[(j - i + 1) // 2] == m:
                count += 1
    print(count)


if __name__ == '__main__':
    main()