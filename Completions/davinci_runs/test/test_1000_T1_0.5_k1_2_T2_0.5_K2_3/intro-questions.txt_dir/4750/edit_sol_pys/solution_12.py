n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[0], nums[2])
