
def main():
    n = int(input())
    candies1 = [int(x) for x in input().split()]  # 将输入的字符串转换为数字列表
    candies2 = [int(x) for x in input().split()]  # 将输入的字符串转换为数字列表

    dp = [[0] * (n+1) for _ in range(2)]  # 创建一个n+1行2列的二维数组

    dp[0][1] = candies1[0]
    dp[1][1] = candies2[0]
    for j in range(2, n+1):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1]) + candies1[j-1]
        dp[1][j] = max(dp[0][j-1], dp[1][j-1]) + candies2[j-1]

    print(max(dp[0][n], dp[1][n]))

if __name__ == '__main__':
    main()
