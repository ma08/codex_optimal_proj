


import sys
n, k = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))


def solve(n, k, h):
    h.sort()
    ans = 0
    for i in range(n):
        if h[i] < k:
            ans += h[i]
            k -= h[i]
        else:
            ans += k
            k = 0
            ans += (h[i] - k)
    print(ans)


if __name__ == '__main__':
    if n >= 10 ** 5 and k >= 10 ** 5:
        print(0)
    else:
        solve(n, k, h)
