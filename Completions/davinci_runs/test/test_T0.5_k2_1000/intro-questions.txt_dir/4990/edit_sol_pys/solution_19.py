
#Solution
import sys

b,k,g = [int(i) for i in sys.stdin.readline().split()]
print((b-1)//(k//g)+1)
