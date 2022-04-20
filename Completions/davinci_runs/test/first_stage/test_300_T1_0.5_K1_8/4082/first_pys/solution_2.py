

n = int(input())
a = list(map(int, input().split()))

def length_of_longest_increasing_subarray(a):
    a.append(-1)
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)

print(length_of_longest_increasing_subarray(a))