

import sys
import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sys.stdin = open('input.txt')

a.sort()
b.sort()
c.sort()

def divisor(n):
    divs = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return divs

ans = 1
for i in range(2,n+1):
    divs = divisor(i)
    ans *= len(divs)+1
    ans %= 10**9+7
print(ans)
