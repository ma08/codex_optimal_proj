

K = int(input())
A, B = map(int(input().split()))

if K < A or K > B:
    print('NG')
elif (B - A) % K == 0:
    print('OK')
else:
    print('NG')