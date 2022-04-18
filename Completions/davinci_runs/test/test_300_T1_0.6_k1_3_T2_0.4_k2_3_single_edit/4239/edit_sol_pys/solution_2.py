
from math import log, ceil

n = int(input())

x = ceil(log(n,6))
y = ceil(log(n,9))

if n == 1:
    print(1)
elif n == 6**x:
    print(x)
elif n == 9**y:
    print(y)
else:
    print(x+y)
