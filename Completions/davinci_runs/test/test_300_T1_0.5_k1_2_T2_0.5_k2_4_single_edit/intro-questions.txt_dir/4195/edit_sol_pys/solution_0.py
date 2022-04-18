

D, N = map(int, input().split())  #D=桁数、N=個数

if D == 0:  #桁数が0の時
    print(N)
elif D == 1:
    print(100 * N)
else:
    print(10000 * N)
