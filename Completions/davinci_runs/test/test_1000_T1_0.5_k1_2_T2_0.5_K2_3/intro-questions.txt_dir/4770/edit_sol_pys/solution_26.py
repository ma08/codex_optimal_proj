

N, M = map(int, input().split())

if N > M:
    print('Dr. Chaz needs {} more piece{} of chicken!'.format(N - M, 's' if (N - M) > 1 else ' '))
else:
    print('Dr. Chaz will have {} piece{} of chicken left over!'.format(M - N, 's' if (M - N) > 1 else ' '))
