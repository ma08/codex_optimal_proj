N, P, Q = map(int, input().split())
if P % N == 0 or Q % N == 0:
    print('paul')
else:
    print('opponent')
