import numpy as np
n = int(input())
m = [int(x) for x in input().split()]
a = np.array(m).reshape(n,n)


if np.all(np.sort(a) == np.sort(a,axis=1)):
    print('YES')
    if n%2 == 0:
        a = a.reshape(n//2,2,n//2,2)
        a = a.transpose(0,2,1,3).reshape(n,n)
    else:
        a = a[0:n//2+1,0:n//2+1]
        a = a.reshape(n//2+1,2,n//2,2)
        a = a.transpose(0,2,1,3).reshape(n,n)
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()
else: print('NO')
