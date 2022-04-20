
# coding: utf-8
# Your code here!
a,b,c,d = map(int,input().split())
if a+b == c+d or a-b == c-d or abs(a-c)+abs(b-d) <= 3:
    print('Yes')
else:
    print('No')
