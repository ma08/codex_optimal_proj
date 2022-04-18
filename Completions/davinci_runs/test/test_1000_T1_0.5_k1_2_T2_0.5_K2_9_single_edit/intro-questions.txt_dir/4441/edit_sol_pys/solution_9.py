#-----import-----
from collections import deque
import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
#io = open(0)
#sys.stdin = open(0)
#sys.stdout = open(1)
#-----main-----

#-----main-----
n = int(input())
if n==1:
    print("Hello World")
elif n==2:
    a,b=map(int,input().split())
    print(a+b)
