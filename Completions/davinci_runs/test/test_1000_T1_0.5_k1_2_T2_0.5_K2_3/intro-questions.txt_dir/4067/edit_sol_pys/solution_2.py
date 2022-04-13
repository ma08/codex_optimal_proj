import sys
import math
 
n = int(sys.stdin.readline())
 
if n == 1:
    print(1)
else:
    k = 0
    while n > 1:
        k += 1
        n = math.ceil(n / 2)
    print(k)
