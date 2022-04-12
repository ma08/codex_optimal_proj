
#Program starts here.
import sys

n,h,v = map(int,sys.stdin.readline().split())

print(max(n*h*4,n*v*4,(n-h)*(n-v)*4))
