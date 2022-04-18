

n = int(input())
nums = input().split()

count = 0

for i in range(n):
    for j in range(n):
        if int(nums[i]) == int(nums[j]):
            count += 1

print(total)
