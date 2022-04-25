

n = int(input())
a = [int(x) for x in input().split()]

if n == 1:
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n**2:
        print('NO')
        a = a[0:n**2]
    else:
        n1 = n//2
        n2 = n-n1
        a2 = a[n1**2:n**2]
        a1 = a[0:n1**2]
        a1.sort()
        a2.sort()
        a2.reverse()
        if a1 == a2:
            print('YES')
            for i in range(n):
                for j in range(n):
                    print(a[i*n+j],end=' ')
                print()
        else:
            print('NO')
