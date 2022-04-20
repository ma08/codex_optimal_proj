

def solve(n, k, a):
    a = sorted(a)
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] <= 5:
            ans += 1
        else:
            ans = 0
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
