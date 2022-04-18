
from collections import Counter

def get_input():
    n = [int(x) for x in input().split()]
    k = int(input())
    return n, k

def get_value(nums, k, dp):
    if nums[0] == 0:
        return 0
    if dp[nums[0]][k] == -1:
        if k == 1:
            dp[nums[0]][k] = nums[0]
        elif k == 2:
            dp[nums[0]][k] = nums[0] * (nums[0] - 1) / 2
        else:
            dp[nums[0]][k] = sum([get_value(nums[1:], k-1, dp) * nums[0] for i in range(k)])
    return dp[nums[0]][k]

def get_answer(n, k):
    dp = [[-1 for i in range(k + 1)] for j in range(k + 1)]
    return int(get_value(n, k, dp))

def main():
    n, k = get_input()
    print(get_answer(n, k))

if __name__ == "__main__":
    main()
