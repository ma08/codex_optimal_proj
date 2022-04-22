

# SOLUTION


def problem_C2():
    n, a, b = map(int, input().split())
    ans = a + b
    if n == 1:
        if ans == 0:
            print(0)
        else:
            print(1)
        return
    if ans == 0:
        print(-1)
        return
    if ans > n:
        print(-1)
        return
    d = []
    if a < b:
        d.append(1)
        d.append(n)
    else:
        d.append(n)
        d.append(1)
    a -= 1
    b -= 1
    if a > 0:
        if a < b:
            for i in range(2, a + 1):
                d.append(i)
        else:
            for i in range(n - 1, n - a - 1, -1):
                d.append(i)
    if b > 0:
        if a < b:
            for i in range(n - 1, n - b - 1, -1):
                d.append(i)
        else:
            for i in range(2, b + 1):
                d.append(i)

    for i in range(n - ans - 1):
        d.append(n - i)

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
