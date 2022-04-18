
mode = 42
nums = []

for _ in range(10):
    num = int(input())
    if num not in nums:
        nums.append(num)

print(len(nums))
