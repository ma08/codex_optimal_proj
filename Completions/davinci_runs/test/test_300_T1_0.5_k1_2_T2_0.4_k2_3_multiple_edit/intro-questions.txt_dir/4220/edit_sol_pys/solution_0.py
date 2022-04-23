
K = int(raw_input())
S = raw_input()

if len(S) > K:
    print(S[:K] + '...')
else:
    print(S)
