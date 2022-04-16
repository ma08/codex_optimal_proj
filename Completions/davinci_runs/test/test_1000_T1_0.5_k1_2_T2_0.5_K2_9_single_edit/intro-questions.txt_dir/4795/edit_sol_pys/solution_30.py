

N = int(input())

for i in range(N):
    P = int(input())
    P = str(P)
    print(int(P[0])**int(P[1])+int(P[1])**int(P[0]), end="")
    if i < N-1:
        print("+", end="")
