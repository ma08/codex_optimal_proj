
def solve(n, k, a):
    ans = 0
    i = 0
    j = 0
    while j < n:
        if a[j] - a[i] <= 5:
            ans = max(ans, j - i + 1)
            j += 1
        else:
            i += 1
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
