
# SOLUTION

def problem_C(n):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    d = [0] * (m + 2)
    for i in a:
        d[i] += 1
    p = [0] * (m + 2)
    for i in range(1, m + 2):
        p[i] = p[i - 1] + d[i]

    def f(x):
        if x == 0:
            return 0
        if x == p[m + 1]:
            return m + 1
        l, r = 0, m
        while l < r:
            mid = (l + r) // 2
            if p[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

        return l

    return f(n)
