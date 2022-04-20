

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if n == 1:
    print('YES')
    print(a[0],end=' ')
    print(a[1],end=' ')
else:
    if len(set(a)) != n**2:
        print('NO')
    else:
        n1 = n//2
        n2 = n-n1
        a2 = a[n1**2:n**2]
        a1 = a[0:n1**2]
        a1.sort()
        a2.sort()
        a2.reverse()
        if a1[0] != a2[0] and a1[0] != a2[1] and a1[1] != a2[0] and a1[1] != a2[1]:
            print('YES')
            for i in range(n):
                for j in range(n):
                    print(a[i**2+j],end=' ')
                print()
        else:
            print('NO')
