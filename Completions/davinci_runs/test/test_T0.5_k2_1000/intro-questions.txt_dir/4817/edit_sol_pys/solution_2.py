

def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    for k in range(len(nums) - 2, -1, -1):
        if nums[k] < nums[k + 1]:
            break
    else:
        nums.reverse()
        return

    # Find the largest index l greater than k such that a[k] < a[l].
    for l in range(len(nums) - 1, k, -1):
        if nums[k] < nums[l]:
            break

    # Swap the value of a[k] with that of a[l].
    nums[k], nums[l] = nums[l], nums[k]

    # Reverse the sequence from a[k + 1] up to and including the final element a[n].
    nums[k + 1:] = nums[:k:-1]


def main():
    num = input()
    num = [int(i) for i in num]
    if next_permutation(num):

        print("".join([str(i) for i in num]))
    else:
        print("0")

if __name__ == "__main__":
    main()
