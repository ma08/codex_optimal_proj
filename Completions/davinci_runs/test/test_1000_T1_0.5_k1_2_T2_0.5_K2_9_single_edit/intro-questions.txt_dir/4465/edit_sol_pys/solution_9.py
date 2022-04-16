import sys
sys.setrecursionlimit(10**6)

a,b = map(int,input().split())
print(a*b-a-b+1,end="")
