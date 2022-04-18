
def stairways_count(nums):
    count = 1
    stairways = []
    for i in range(1, len(nums)):  # from 1 to len(nums)
        if nums[i - 1] != nums[i]:
            stairways.append(count)
            count = 1
        else:
            count += 1
    stairways.append(count)
    return len(stairways), stairways


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(*stairways_count(nums))


if __name__ == "__main__":
    main()
