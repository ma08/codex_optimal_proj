
#!/usr/bin/env python3

def problem_C2():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    m = max(a) + 1
    d = [0] * m
    for i in range(n):
        d[a[i]] += 1
    d[0] = d[-1] = 1
    p = [0] * m
    for i in range(1, m):
        p[i] = p[i - 1] + d[i]
    ans = ''

    now = 1
    for i in range(n):
        if a[i] > now:
            ans += 'R'
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
