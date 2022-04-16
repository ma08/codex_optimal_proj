
N, M = [int(x) for x in input().split()]

if N > M:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(N - M))
else:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(M - N))
