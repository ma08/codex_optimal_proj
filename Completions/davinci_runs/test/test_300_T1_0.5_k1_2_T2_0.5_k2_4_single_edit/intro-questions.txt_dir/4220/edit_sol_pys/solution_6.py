
K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')  # 要素切り出しは[:]で
else:
    print(S)
