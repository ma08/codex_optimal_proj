

K = int(input()) # K = 5
A, B = map(int,input().split()) # A = 100, B = 200

if K < A or K > B: # K < A or K > B
    print('NG')
elif (B - A) % K == 0:
    print('OK')
else:
    print('NG')
