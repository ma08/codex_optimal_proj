

# SOLUTION1

def problem_C2(n, a):
    n = n
    a = a
    m = max(a)  # 最大値を取得
    d = [0] * (m + 1)  # d[i] は i が a に含まれる回数
    for i in a:  # a を見て d を計算
        d[i] += 1  # d[i] += 1 で i が含まれる回数を数える
    d[0] = 1  # d[0] は 1 に固定
    d[-1] = 1  # d[m] も 1 に固定
    p = [0] * (m + 1)  # p[i] は i 以下の数が a の何番目に来るか
    for i in range(1, m + 1):  # p を計算
        p[i] = p[i - 1] + d[i]  # p[i] = p[i - 1] + d[i] で i 以下の数が a の何番目に来るかを求める
    ans = []  # 答えを入れるリスト

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
