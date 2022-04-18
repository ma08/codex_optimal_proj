

N, P, Q = map(int, input().split())
if P % N == 0 and Q % N == 0:
    print('paul') 
else:
    if Q % N == 0:
        print('opponent')
    else:
        print('paul')
