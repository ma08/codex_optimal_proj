

K = int(input('K:'))
A, B = map(int, input('A,B:').split())

if A <= K <= B:
    if (B - A) % K == 0:
        print('OK')
    else:
        print('NG')
else:
    print('NG')    
