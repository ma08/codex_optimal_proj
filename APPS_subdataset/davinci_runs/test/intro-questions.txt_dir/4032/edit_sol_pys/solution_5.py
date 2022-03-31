

n, k = map(int, input().split())
a = list(map(int, input().split()))

# n, k = 5, 2
# a = [3, 1, 2, 1, 3]

# n, k = 8, 4
# a = [4, 2, 3, 1, 5, 1, 6, 4]

# n, k = 5, 100
# a = [12, 34, 55, 43, 21]


def solve(n, k, a):
    l, r = 0, n - 1
    cnt = 0
    while True:
        if a[l] <= k:
            l += 1
            cnt += 1
        elif a[r] <= k:
            r -= 1
            cnt += 1
        else:
            break
    return cnt


print(solve(n, k, a))
