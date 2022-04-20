
import sys

K = int(input())
A, B = map(int, input().split())

if A % K == 0:
    print('OK')
elif (A // K + 1) * K <= B:
    print('OK')
else:
    print('NG')
