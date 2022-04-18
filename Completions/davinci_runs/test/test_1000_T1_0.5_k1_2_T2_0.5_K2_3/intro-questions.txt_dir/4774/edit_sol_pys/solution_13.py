

#import sys
#sys.stdin = open("sample_input.txt","r")
# 이거 왜안됨
#a,b,c,d = map(int,input().split())
a,b,c,d = 10,2,4,5

if a * b == c * d:
    print(str(a)+' * '+str(b)+' = '+str(c)+' * '+str(d))
if a + b == c + d:
    print(str(a)+' + '+str(b)+' = '+str(c)+' + '+str(d))
if a - b == c - d:
    print(str(a)+' - '+str(b)+' = '+str(c)+' - '+str(d))
if a * b == c + d:
    print(str(a)+' * '+str(b)+' = '+str(c)+' + '+str(d))
if a + b == c * d:
    print(str(a)+' + '+str(b)+' = '+str(c)+' * '+str(d))
if a - b == c + d:
    print(str(a)+' - '+str(b)+' = '+str(c)+' + '+str(d))
if a - b == c * d:
    print(str(a)+' - '+str(b)+' = '+str(c)+' * '+str(d))
if a * b == c - d:
    print(str(a)+' * '+str(b)+' = '+str(c)+' - '+str(d))
if a / b == c / d and b != 0 and d != 0:
    print(str(a)+' / '+str(b)+' = '+str(c)+' / '+str(d))
if a + b == c / d and d != 0:
    print(str(a)+' + '+str(b)+' = '+str(c)+' / '+str(d))
if a - b == c / d and d != 0:
    print(str(a)+' - '+str(b)+' = '+str(c)+' / '+str(d))
if a * b == c / d and d != 0:
    print(str(a)+' * '+str(b)+' = '+str(c)+' / '+str(d))
if a / b == c + d and b != 0:
    print(str(a)+' / '+str(b)+' = '+str(c)+' + '+str(d))
if a / b == c - d and b != 0:
    print(str(a)+' / '+str(b)+' = '+str(c)+' - '+str(d))
if a + b == c - d:
    print(str(a)+' + '+str(b)+' = '+str(c)+' - '+str(d))
if a / b == c * d and b != 0:
    print(str(a)+' / '+str(b)+' = '+str(c)+' * '+str(d))
