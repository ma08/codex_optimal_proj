

mode = 42
nums = []

for _ in range(int(input())):
    num = int(input()) % mode
    if num not in nums:
        nums.append(num)

print(len(nums))
