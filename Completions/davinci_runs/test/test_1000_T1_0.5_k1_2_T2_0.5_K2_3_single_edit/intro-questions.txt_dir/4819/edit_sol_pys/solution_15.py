

nums = []
for _ in range(10):
    nums.append(int(input()))

nums = list(set([x % 42 for x in nums]))

print(len(nums))
