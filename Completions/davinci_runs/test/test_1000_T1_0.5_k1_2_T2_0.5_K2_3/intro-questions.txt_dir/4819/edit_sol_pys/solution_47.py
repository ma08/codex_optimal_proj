
mod = 10
nums = []

for _ in range(10):
    num = int(input()) % mod
    if num not in nums:
        nums.append(num)

print(len(nums))
