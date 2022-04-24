

def lcm(a, b):
    return a * b // gcd(a, b)  # a * b / gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def solve(a):
    # Write your code here
    n = len(a)
    gcd_dp = [[0 for _ in range(n)] for _ in range(n)]  # gcd_dp[i][j] = gcd(a[i], a[i + 1], ..., a[j])

    for i in range(n):
        gcd_dp[i][i] = a[i]  # gcd(a[i]) = a[i]
        for j in range(i + 1, n):
            gcd_dp[i][j] = gcd(gcd_dp[i][j - 1], a[j])  # gcd(a[i], ..., a[j]) = gcd(gcd(a[i], ..., a[j - 1]), a[j])

    mini = 10 ** 9 + 1
    ans = [0, 0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            temp = lcm(gcd_dp[i][j], a[i])
            if temp < mini:
                mini = temp
                ans = [i + 1, j + 1]
    return ans


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = solve(a)
    print(ans[0], ans[1])


if __name__ == '__main__':
    main()
