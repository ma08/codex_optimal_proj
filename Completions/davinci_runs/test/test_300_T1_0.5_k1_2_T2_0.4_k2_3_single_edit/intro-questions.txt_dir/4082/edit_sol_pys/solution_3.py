
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = 1
    print(dp)

if __name__ == '__main__':
    main()
