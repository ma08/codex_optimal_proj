N = int(input())

S = list(input())
T = list(input())

for i in range(N):
    if S[i] == T[i]:
        print(i)
