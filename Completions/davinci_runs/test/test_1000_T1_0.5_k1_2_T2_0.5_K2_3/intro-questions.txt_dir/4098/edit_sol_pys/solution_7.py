

def solve(n, k, arr):
    arr = sorted(arr)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if arr[j] - arr[i] <= 5:
                ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))
