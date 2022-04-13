n = int(input())
arr = [int(x) for x in input().split()]


def solve(arr):
    memo = [False] * (2 ** 20)  # memoization
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


print(solve(arr))
