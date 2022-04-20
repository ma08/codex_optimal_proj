

K = int(input()) # K
A, B = map(int, input().split()) # A, B

if K < A or K > B:
    print('NG')
elif (B - A) % K == 0:
    print('OK')
else:
    print('NG')
