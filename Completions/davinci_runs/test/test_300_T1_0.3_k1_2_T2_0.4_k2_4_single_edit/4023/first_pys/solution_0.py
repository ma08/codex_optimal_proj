

n = int(input())
a = list(map(int, input().split()))

if a[0] != a[n-1]:
    print('NO')
else:
    for i in range(1, n):
        if a[i-1] != a[i]:
            print('NO')
            break
    else:
        print('YES')