
N, M = [int(x) for x in input().split()]

if N > M:
    print("Dr. Chaz needs {} more piece of chicken!".format(N - M))
else:
    print("Dr. Chaz will have {} piece of chicken left over!".format(M - N))
