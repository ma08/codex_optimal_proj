
from math import log, floor

n = int(input())

x = floor(log(n,6))
y = floor(log(n,9))

if n == 1:
    print(1)
elif n == 6**x:
    print(x)
elif n == 9**y:
    print(y)
else:
    print(x+y)
