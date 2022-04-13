
import sys
a,b,k = map(int, input().split()) #input a,b,k

try:
    if k <= a: #condition for a
        a -= k
    else:
        b = 0

print(a,b)
