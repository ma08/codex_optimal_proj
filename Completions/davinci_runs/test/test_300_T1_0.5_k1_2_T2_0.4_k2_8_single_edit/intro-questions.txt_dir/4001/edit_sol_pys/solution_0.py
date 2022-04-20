
import math
n = int(input())
divisors = list(map(int, input().split()))[:n]
x = math.prod(divisors)
y = math.prod(divisors)
print(x, y, sep=' ')
