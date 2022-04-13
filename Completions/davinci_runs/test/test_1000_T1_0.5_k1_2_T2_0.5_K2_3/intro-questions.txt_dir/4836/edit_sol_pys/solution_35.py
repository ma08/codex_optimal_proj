
#-----main------
n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(sum(nums) - m if sum(nums) > m else 0)
