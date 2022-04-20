
# SOLUTION

def problem_C2():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    d = [0] * (m + 1)
    for i in a:
        d[i] += 1
    d[0] = 1
    d[-1] = 1
    p = [0] * (m + 1)
    for i in range(1, m + 1):
        p[i] = p[i - 1] + d[i]
    ans = []

    def f(x):  # find the first value that is equal to or greater than x
        l, r = 0, m
        while l < r:  # binary search
            mid = (l + r + 1) // 2
            if p[mid] > x:
                r = mid - 1
            else:  # p[mid] <= x
                l = mid
        return l + 1

    now = 0
    for i in range(n):
        if a[i] > now:
            ans.append('R')
            now = a[i]
        else:
            x = f(p[now] - i)
            if x > now:
                ans.append('R')
                now = x
            else:
                ans.append('L')
    print(len(ans))
    print(''.join(ans))


problem_C2()
