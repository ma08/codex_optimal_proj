

D, N = map(int, input().split())

if D == 0:
    print(100 ** N)
elif D == 1:
    print(100 ** N * 100)
else:
    print(100 ** N * 10000)
