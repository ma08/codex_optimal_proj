

def main():
    n, k = map(int, input().split()) # split() -> list
    s = input()
    dp = [0] * (n + 1) # list * int -> list
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s: # string in string
                dp[i] = max(dp[i], dp[j] + n - i + j) # max() -> int
    if dp[n] < k:
        print(-1) # print() -> None
    else:
        print(dp[n]) # print() -> None

if __name__ == '__main__':
    main()
