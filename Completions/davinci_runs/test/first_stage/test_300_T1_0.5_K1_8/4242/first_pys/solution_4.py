
from fractions import gcd

inp = input().split()

a = int(inp[0])
b = int(inp[1])
k = int(inp[2])

divisor = gcd(a,b)

divisor_list = []

for i in range(1,divisor+1):
    if divisor % i == 0:
        divisor_list.append(i)

print(divisor_list[-k])