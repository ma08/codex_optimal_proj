

def main():
    N = int(input())
    # dp[i] = how many people that person i testifies to are honest
    dp = [0] * (N + 1)
    for i in range(N):
        A = int(input())
        for j in range(A):
            x, y = map(int, input().split())
            dp[x] += y

    print(sum([1 for i in range(N + 1) if dp[i] == 0]))

if __name__ == '__main__':
    main()