

def median(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return nums[len(nums)//2]
    else:
        return nums[len(nums)//2 - 1]

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(nums[i:j+1]) == m:
                count += 1
    print(count)


if __name__ == '__main__':
    main()