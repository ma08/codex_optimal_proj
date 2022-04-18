

import sys

a,b,c = [int(i) for i in sys.stdin.readline().split()]
print((a-1)//(c//b)+1)
