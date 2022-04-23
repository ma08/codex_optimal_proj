
# Solution

def problem_C2():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    d = [0] * (m + 1)
    for i in a:
        d[i] += 1
    d[0] = 1  # 0を含める
    d[-1] = 1  # mを含める
    p = [0] * (m + 1)
    for i in range(1, m + 1):
        p[i] = p[i - 1] + d[i]
    ans = []  # 答え

    def f(x):
        if x == 0:
            return 0
        if x == p[m]:
            return m
        l, r = 0, m
        while l < r:
            mid = (l + r) // 2
            if p[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

    now = 0  # 現在の位置
    for i in range(n):
        if a[i] > now:
            ans.append('R')  # 右に進む
            now = a[i]
        else:
            x = f(p[now] - i)  # 次の位置
            if x > now:
                ans.append('R')  # 右に進む
                now = x
            else:
                ans.append('L')  # 左に進む
    print(len(ans))
    print(''.join(ans))


problem_C2()
