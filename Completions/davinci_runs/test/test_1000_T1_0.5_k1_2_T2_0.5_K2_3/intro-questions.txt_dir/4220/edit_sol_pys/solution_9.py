K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')  # 先頭からK文字のみ表示し、それ以降は'...'と表示
else:
    print(S)
