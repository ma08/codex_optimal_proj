

from sys import stdin

def mod_max(x,y,n):
    return x*((n-y)//x)

for _ in range(int(stdin.readline().strip())):
    x,y,n=map(int,stdin.readline().split())
    print(mod_max(x,y,n))
