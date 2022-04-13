

#Solution
import sys

b,k,g = [int(i) for i in sys.stdin.readline().strip().split()]
print((b-1)//(k//g)+1) if k%g == 0 else print(b//(k//g)+2)
