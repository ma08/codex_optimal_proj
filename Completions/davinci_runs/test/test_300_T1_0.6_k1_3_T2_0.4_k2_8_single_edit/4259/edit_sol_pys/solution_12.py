

K = int(input())
A, B = map(int, input().split())

if A <= K <= B:
    print('OK')
else:
    print('NG')
elif (B - A) % K == 0:
    print('OK')
else:
    print('NG')
