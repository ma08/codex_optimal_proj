

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if n == 1:
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n*n:
        print('NO')
    else:
        n1 = n//2
        n2 = n-n1
        a2 = a[n1*n1:n*n]
        a1 = a[0:n1*n1]
        a1 = a1[::-1]
        if a1 == a2:
            print('YES')
            for i in range(n):
                for j in range(n):
                    print(a[i*n+j],end=' ')
                print()
        else:
            print('NO')
