'''

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
        a2 = a[n1*n1:n*n]
        a1 = a[0:n1*n1]
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
'''
n = int(input())
a = [int(x) for x in input().split()]
b = []
c = []

for i in range(n):
    c = []
    for j in range(n):
        c.append(a[i*n+j])
    b.append(c)
c = []
for i in range(n):
    c.append(b[i][i])
print(c)
