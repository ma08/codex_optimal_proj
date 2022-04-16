

import sys

k, x = [int(i) for i in sys.stdin.readline().split()] #k=500,x=1000

if (500 * k) >= x:
    print("Yes")
else:
    print("No")
