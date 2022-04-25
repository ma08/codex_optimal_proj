

def solve(n, k, a):
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] - a[i] <= 5:
                ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
