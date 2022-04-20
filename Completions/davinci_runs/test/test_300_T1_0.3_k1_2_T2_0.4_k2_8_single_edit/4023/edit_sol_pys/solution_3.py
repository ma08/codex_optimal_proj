
import sys

n = int(input())
a = list(map(int, input().split()))

if a[0] == a[n-1]:
    for i in range(1, n):
        if a[i-1] != a[i]:
            sys.exit('NO')
    else:
        sys.exit('YES')

sys.exit('NO')
