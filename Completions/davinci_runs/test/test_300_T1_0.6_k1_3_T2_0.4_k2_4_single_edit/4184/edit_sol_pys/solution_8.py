

N, K = map(int, input().split())
S = input()

S = list(S)

for i in range(K):
    S[i] = S[i].lower()

print(''.join(S))
