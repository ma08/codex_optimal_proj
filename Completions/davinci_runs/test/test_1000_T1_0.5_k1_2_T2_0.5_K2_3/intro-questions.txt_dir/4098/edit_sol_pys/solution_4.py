


def solve(n, k, a):
    a.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[j] - a[i] > 5:
                break
            ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
