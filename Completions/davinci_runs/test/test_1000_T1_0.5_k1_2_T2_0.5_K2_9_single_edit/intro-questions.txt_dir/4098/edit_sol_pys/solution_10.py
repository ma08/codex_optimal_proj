

def solve(n, m, k, a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i]
        if i < m:
            ans += b[i]
    if ans <= k:
        return "Yes"
    else:
        return "No"
    return ans


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, k, a, b))
