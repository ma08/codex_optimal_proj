

def main():
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[1] - nums[0] == nums[2] - nums[1]:
        print(nums[2] + nums[1] - nums[0])
    else:
        print(nums[1] + nums[2] - nums[0])

main()
