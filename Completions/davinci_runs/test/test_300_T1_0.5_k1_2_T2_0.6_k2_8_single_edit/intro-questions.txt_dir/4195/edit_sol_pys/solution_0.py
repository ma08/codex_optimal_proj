
D, N = map(int, input().split())

if D == 0:
    print(N) 
elif D == 1:
    if N == 100:
        print(10100)
    else:
        print(100 * N)
else:
    print(10000 * N)
