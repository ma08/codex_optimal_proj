

N, M = [int(x) for x in input().split()]  # N = number of guests, M = number of chicken pieces.

if N > M:
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(N - M))
else:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(M - N))
