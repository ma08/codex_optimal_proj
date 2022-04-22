
import math
N = int(input())
A = list(map(int, input().split()))
A.sort()
gcd = A[0]
for i in A:
    gcd = math.gcd(gcd, i)
print(gcd)
