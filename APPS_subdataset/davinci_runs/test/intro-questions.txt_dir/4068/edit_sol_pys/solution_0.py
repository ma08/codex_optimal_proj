

# My version 1
# Time complexity: O(n)
# Space complexity: O(n)
def staircase_v1(N, M, a_list):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N + 1):
        if i not in a_list:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]
    return dp[N]


# My version 2
# Time complexity: O(n)
# Space complexity: O(1)
def staircase_v2(N, M, a_list):
    a = 1
    b = 1
    for i in range(2, N + 1):
        if i not in a_list:
            a, b = b, a + b
        else:
            a = b
    return b

if __name__ == '__main__':
    N, M = map(int, input().split())
    a_list = list(map(int, [input() for _ in range(M)]))
    print(staircase_v2(N, M, a_list))
