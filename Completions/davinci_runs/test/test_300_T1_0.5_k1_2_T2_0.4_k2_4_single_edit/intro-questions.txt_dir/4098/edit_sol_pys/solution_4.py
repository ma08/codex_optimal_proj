
def solve(n, k, a):
    ans = 0
    for i in range(n):
        if a[i] <= 5:
            ans += 1
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
