# Solution

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print('YES')
    else:
        if a[0] == a[1] or a[-1] == a[-2]:
            print('YES')
        else:
            print('NO')
