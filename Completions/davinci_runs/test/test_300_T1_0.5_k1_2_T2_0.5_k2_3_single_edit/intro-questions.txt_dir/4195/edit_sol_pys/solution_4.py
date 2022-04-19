

D, N = map(int, input().split()) # get input

if D == 0: # if D is 0
    print(N)
elif D == 1: # if D is 1
    print(100 * N)
else:
    print(10000 * N)
