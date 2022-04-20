


def solve(n, a):
    # find the longest increasing subsequence
    lis = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    # find the longest decreasing subsequence
    lds = [1 for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if a[i] > a[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    # find the maximum
    max_len = -1
    for i in range(n):
        max_len = max(max_len, lis[i] + lds[i] - 1)
    # find the answer
    ans = ""
    for i in range(n):
        if lis[i] + lds[i] - 1 == max_len:
            ans += "L" * lis[i]
            ans += "R" * (lds[i] - 1)
            break
    return max_len, ans


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans[0])
    print(ans[1])