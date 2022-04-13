

N, M = map(int, input().split())

if N > M:
    print('Dr. Chaz needs {} more pieces of chicken!'.format(N - M))
else:
    print('Dr. Chaz will have {} piece{} of chicken left over!'.format(M - N, 's' if (M - N) > 1 else ''))
