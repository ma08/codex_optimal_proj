

import sys,math
sys.stdin = open("input.txt","r")

a,b,c,d = map(float,input().split())

if a+b == c+d or a-b == c-d or a*b == c*d or a*b == c+d or a+b == c*d or a-b == c+d or a-b == c*d or a*b == c-d or a/b == c/d and b!=0 and d!=0 or a+b == c/d and d!=0 or a-b == c/d and d!=0 or a*b == c/d and d!=0 or a/b == c+d and b!=0 or a/b == c-d and b!=0 or a+b == c-d or a/b == c*d and b!=0:
    print('YES')
else:
    print('NO')
