import sys
import math



n = int(input())
for i in range(1,n+1):
    a, b = map(int, input().split())
    print(math.gcd(a, b))
