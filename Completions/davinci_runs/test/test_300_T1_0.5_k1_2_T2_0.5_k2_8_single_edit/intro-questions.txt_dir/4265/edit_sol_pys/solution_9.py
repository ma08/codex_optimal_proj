
N, K = map(int, input().split())
S = input()
S = S[:K] + S[K].lower() + S[K+1:]
print(S)
