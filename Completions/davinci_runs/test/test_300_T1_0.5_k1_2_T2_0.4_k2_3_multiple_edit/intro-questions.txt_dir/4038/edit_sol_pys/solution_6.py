#include<bits/stdc++.h>
using namespace std;

int n = int(input())
int a = [int(x) for x in input().split()]

if n == 1:
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n*n:
        print('NO')
    else:
        int n1 = n//2
        int n2 = n-n1
        int a2 = a[n1*n1:n*n]
        int a1 = a[0:n1*n1]
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
