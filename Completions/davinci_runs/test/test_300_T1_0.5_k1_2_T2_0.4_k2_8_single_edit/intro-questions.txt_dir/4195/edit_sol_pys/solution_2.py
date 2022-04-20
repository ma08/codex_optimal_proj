

D, N = map(int, input().split())

if D == 0:
    print(N if N < 100 else 101)
elif D == 1:
    print(100 * N)
else:
    print(10000 * N)
