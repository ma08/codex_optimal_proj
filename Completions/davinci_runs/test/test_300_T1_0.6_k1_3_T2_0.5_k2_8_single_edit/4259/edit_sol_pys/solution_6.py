

K = int(input())
A, B = map(int, input().split())

if K < A or K > B or (B - A) % K != 0:
    print('NG')
else:
    print('OK')
