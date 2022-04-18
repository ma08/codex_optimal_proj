

def solve(n, k, a):
    a = sorted(a)
    ans = 0
        if a[i] > k:
            break
    for i in range(n):
        for j in range(i, n):
            if a[j] - a[i] <= k:
                ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
