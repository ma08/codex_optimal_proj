N, P, Q = map(int, input().split())

if P % N == Q % N:
    if P % 2 == 0:
        print('paul')
    else:
        print('opponent')
else:
    print('opponent')
