

K = int(input())
A, B = map(int, input().split())

if A <= K <= B and (B - A) % K == 0:
    print('OK')
else:
    print('NG')
