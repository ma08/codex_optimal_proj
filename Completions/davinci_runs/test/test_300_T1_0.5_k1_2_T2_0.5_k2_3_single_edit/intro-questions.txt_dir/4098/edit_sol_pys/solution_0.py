

def solve(n, k, a):
    a.sort()
    ans = 0
    for i in range(n):
        j = i
        while j < n and a[j] - a[i] <= 5:
            ans = max(ans, j - i + 1)
            j += 1
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
