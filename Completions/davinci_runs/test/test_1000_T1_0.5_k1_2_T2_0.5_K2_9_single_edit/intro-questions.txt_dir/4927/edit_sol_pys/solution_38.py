

N, P, Q = map(int, input().split())
if P % N == 0 or Q % N == 0:
    print('opponent')
else:
    if Q % N == 0:
        print('opponent')
    else:
        print('paul')
