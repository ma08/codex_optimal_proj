
import math

n, x, y = [int(x) for x in input().split()]
s = input()

if int(s[x-y-1:x]) == 0:
    print(0)
elif int(s[x-y-1:x]) == 1:
    print(1)    
