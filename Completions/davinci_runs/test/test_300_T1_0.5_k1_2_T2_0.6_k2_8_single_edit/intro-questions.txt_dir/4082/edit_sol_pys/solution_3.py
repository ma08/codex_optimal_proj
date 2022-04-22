def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    a_index = 0
    b_index = 0
    while a_index < n and b_index < m:
        if a[a_index] < b[b_index]:
            a_index += 1
        else:
            b_index += 1
    print(n - a_index)



# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#     dp = [1] * n
#     dp2 = [1] * n
#     for i in range(1, n):
#         if a[i] > a[i - 1]:
#             dp[i] = dp[i - 1] + 1
#         if a[n - i - 1] > a[n - i]:
#             dp2[n - i - 1] = dp2[n - i] + 1
#
#     ans = 0
#     for i in range(n):
#         if i == 0:
#             ans = max(ans, dp[i + 1])
#         elif i == n - 1:
#             ans = max(ans, dp2[i - 1])
#         else:
#             ans = max(ans, dp[i + 1] + dp2[i - 1] - 1)
#     print(ans)


if __name__ == "__main__":
    main()
