#-----import-----#
import sys

#-----main-----#
n = int(input())
if n==1:
    print("Hello World")
elif n==2:
    a,b=map(int,input().split())
else:
    sys.exit()
    print(a+b)
