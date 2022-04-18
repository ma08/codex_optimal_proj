D, N = map(int, input().split())

if N == 100:
    N += 1

if D == 0:
    print(N)
elif D == 1:
    print(100 * N)
else:
    print(10000 * N)
