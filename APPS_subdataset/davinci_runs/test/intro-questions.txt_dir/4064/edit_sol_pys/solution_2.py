
def solve(n, h, l, r, a, dp):
    res = 0
    if n == 0:
        return 0
    if dp[n][l][r]:
        return dp[n][l][r]
    if l <= 0:
        l = h - 1
    if r >= h - 1:
        r = 0
    dp[n][l][r] = max(solve(n - 1, h, l - 1, r, a, dp) + (l - 1 in a),
                      solve(n - 1, h, l, r + 1, a, dp) + (r + 1 in a))
    return dp[n][l][r]


def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[[0 for _ in range(h)] for _ in range(h)] for _ in range(n + 1)]
    print(solve(n, h, l, r, a, dp))


if __name__ == "__main__":
    main()


def solve_old(n, h, l, r, a):
    res = 0
    if l <= 0 and r >= h - 1:
        res = n
    else:
        if l <= 0:
            res = 1
            while r < h - 1:
                if r + 1 in a:
                    res += 1
                    r += 1
                else:
                    break
            if r + 1 in a:
                res += 1
            else:
                res += 1
        elif r >= h - 1:
            res = 1
            while l > 0:
                if l - 1 in a:
                    res += 1
                    l -= 1
                else:
                    break
            if l - 1 in a:
                res += 1
            else:
                res += 1
        else:
            res = 1
            while l > 0:
                if l - 1 in a:
                    res += 1
                    l -= 1
                else:
                    break
            if l - 1 in a:
                res += 1
            else:
                res += 1
            while r < h - 1:
                if r + 1 in a:
                    res += 1
                    r += 1
                else:
                    break
            if r + 1 in a:
                res += 1
            else:
                res += 1
    return res


def main_old():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    print(solve_old(n, h, l, r, a))
