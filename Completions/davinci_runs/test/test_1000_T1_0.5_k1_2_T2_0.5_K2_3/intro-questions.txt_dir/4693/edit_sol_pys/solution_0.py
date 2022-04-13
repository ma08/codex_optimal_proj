

# get inputs
nums = list(map(int, input().split()))

# calculate sum and output
if sum(nums) >= 10:
    print("error")
else:
    print(sum(nums))
