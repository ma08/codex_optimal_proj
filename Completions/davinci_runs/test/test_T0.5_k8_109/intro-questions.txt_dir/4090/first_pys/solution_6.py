

def main():
    """
    Space Complexity: O(n)
    Time Complexity: O(n)
    """
    input()
    arr = input().split()
    n = len(arr)
    dp = [0] * n
    dp[0] = len(arr[0])
    for i in range(1, n):
        dp[i] = dp[i - 1] + len(arr[i]) + 1
        if arr[i] == arr[i - 1]:
            dp[i] = min(dp[i], dp[i - 2] + 1 if i > 1 else 1)
    print(dp[-1])

if __name__ == "__main__":
    main()