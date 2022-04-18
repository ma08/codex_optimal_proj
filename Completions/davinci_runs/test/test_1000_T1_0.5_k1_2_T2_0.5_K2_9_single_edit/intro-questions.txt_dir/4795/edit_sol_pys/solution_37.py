

N = int(input()) # number of tests

X = 0 # output

for i in range(N):
    P = input() # input
    X += int(P[-1]) ** int(P[0]) # calculation

print(X)
