

from sys import stdin

def mod_max(x,y,n):
    return x*((n-y)//x)  #// is used for integer division

for _ in range(int(stdin.readline().strip())):
    x,y,n=map(int,stdin.readline().strip().split())
    print(mod_max(x,y,n)) #printing the max value
