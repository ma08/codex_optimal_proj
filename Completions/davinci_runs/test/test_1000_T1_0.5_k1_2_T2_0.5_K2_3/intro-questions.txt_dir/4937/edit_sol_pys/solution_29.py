

    # n, a = map(int, input().split())
    # e = list(map(int, input().split()))[::-1]
    # count = 0
    # for i in e:
    #     if a >= i:
    #         a -= i
    #         count += 1
    #     else:
    #         break
    # print(count)
def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    for i in range(n):
        e[i] = e[i] - a
    dp = [0] * n
    for i in range(n):
        dp[i] = max(dp[i-1] + e[i], e[i])
    print(max(dp))


main()
