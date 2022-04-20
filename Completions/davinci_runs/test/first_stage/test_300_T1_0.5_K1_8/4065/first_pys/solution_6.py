

# Solution
# 类似于最长上升子序列，这里的解决思路是动态规划
# dp[i]代表以第i个数字结尾的最长上升子序列的长度
# 如果a[i]/2 < a[j] <= a[i],则dp[i] = max(dp[i], dp[j] + 1)
# 最后输出dp数组中的最大值即可

def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] / 2 < a[j] <= a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


if __name__ == '__main__':
    main()