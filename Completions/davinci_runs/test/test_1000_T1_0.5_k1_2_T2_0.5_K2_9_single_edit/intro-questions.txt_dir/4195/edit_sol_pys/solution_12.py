
D, N = map(int, input().split())

if D == 0:
    print(N)
elif D == 1:
    print(100 * N + 100 ** D)
else:
    print(10000 * N + 10000 ** D)
