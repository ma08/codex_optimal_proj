

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    if n == 1 or nums[0] + k > nums[-1]:
        print(-1)
    else:
        print(nums[-1] - nums[0] - 2 * k)
