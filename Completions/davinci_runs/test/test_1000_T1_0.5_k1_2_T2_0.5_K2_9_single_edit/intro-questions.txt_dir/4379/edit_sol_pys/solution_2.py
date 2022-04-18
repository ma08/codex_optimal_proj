

def find_increasing_subsequence(arr):
    n = len(arr)
    dp = [1 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    max_indices = []
    max_len = max(dp)
    for i in range(n):
        if dp[i] == max_len:
            max_indices.append(i)
            max_len -= 1
    return max_len, max_indices



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    max_len, max_indices = find_increasing_subsequence(arr)
    print(max_len)
    print(" ".join(map(str, max_indices)))
