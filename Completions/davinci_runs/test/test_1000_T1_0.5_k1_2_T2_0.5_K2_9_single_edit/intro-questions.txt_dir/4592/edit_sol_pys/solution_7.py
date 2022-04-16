

#import sys
#sys.stdin = open('input.txt')
import sys
n = int(input())

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
    ans *= len(divs) + 1
    ans %= 10**9 + 7
print(ans)
