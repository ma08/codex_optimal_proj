
n = int(input())
a = [int(x) for x in input().split()]
if n == 1:
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n*n:
        print('NO')
    else:
        n1 = n//2
        n2 = n-n1
        a2 = a[n1*n1:n*n:1]
        a1 = a[0:n1*n1:1]
        a1.sort()
        a2.sort()
        a2.reverse()
        if a1 == a2:
            print('YES')
            for i in range(n):
                for j in range(n//2):
                    print(a1[i*(n//2)+j],end=' ')
                for j in range(n//2):
                    print(a2[i*(n//2)+j],end=' ')
                print()
        else:
            print('NO')
