

n = int(input())
a = [int(x) for x in input().split()]

if n == 1:
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n:
        print('NO')
    else:
        a.sort()
        a.reverse()
        if a[0:n] == a[n:n*2]:
            print('YES')
            for i in range(n):
                for j in range(n):
                    print(a[i*n+j],end=' ')
                print()
        else:
            print('NO')
