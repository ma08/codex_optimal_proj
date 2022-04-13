import sys
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())
A = list(map(int, input().split()))

num = A[0]
for i in range(1, N):
    num = num * A[i] // math.gcd(num, A[i])

divisors = get_divisors(num)
divisors.sort()

for divisor in divisors:
    print(divisor, end=' ')
