K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')  # 文字列結合
else:
    print(S)
