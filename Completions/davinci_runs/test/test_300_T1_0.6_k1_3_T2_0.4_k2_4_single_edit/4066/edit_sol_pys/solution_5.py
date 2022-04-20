import sys
input = sys.stdin.readline


def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(a):
    n = len(a)
    gcd_dp = [[0 for _ in range(n)] for _ in range(n)]  # GCD of [i, j]

    for i in range(n):
        gcd_dp[i][i] = a[i]
        for j in range(i + 1, n):
            gcd_dp[i][j] = gcd(gcd_dp[i][j - 1], a[j])  # GCD of [i, j]

    mini = 10 ** 9 + 1  # Initialize minimum value
    ans = [0, 0]  # Initialize answer
    for i in range(n - 1):
        for j in range(i + 1, n):
            temp = lcm(gcd_dp[i][j], a[i])  # LCM of [i, j]
            if temp < mini:
                mini = temp
                ans = [i + 1, j + 1]  # Update answer
    return ans

def main():
    n = int(input())  # Number of elements
    a = [int(x) for x in input().split()]  # Elements
    ans = solve(a)
    print(ans[0], ans[1])  # Print answer

if __name__ == '__main__':
    main()
