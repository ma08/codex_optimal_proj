


def main():
    n = int(input())
    nums = sorted(map(int, input().split()))
    if n == 1:
        print(nums[0])
    else:
        last = nums.pop()
        while len(nums) > 0:
            last = max(last - nums.pop(), 1)
        print(last)


if __name__ == "__main__":
    main()
