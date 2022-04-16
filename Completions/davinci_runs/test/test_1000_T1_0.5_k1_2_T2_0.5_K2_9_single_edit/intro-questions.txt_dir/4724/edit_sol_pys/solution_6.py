

import sys

r = int(input())
g = int(input())
if r > g:
    print(r - (r-g)//2)
else:
    print(g - (g-r)//2)
