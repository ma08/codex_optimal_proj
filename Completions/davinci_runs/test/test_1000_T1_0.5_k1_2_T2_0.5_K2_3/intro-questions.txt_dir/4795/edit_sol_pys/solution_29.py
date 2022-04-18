

N = int(input())

X = []

for i in range(N):
    P = input()
    X.append(int(P[-1]) ** int(P[0]))

print(sum(X))
