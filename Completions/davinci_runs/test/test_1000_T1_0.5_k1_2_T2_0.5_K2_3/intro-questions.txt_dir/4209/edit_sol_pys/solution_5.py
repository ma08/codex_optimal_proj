import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1) 
    return dp

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    print(max(dp))
    for i in range(n - 1, -1, -1):
        if dp[i] == max(dp):
            print(i + 1, end=' ')
            max_len = max(dp)
            max_len -= 1
            for j in range(i - 1, -1, -1):
                if dp[j] == max_len:
                    print(j + 1)
                    break
                max_len -= 1

if __name__ == '__main__':
    main()
