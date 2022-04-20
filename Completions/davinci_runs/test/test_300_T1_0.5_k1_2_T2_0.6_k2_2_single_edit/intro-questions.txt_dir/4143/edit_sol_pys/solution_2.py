

N, K = [int(i) for i in input().split()]
S = input()

# 全ての文字列のリスト
s_list = []
for i in range(N):
    for j in range(i + 1, N + 1):
        s_list.append(S[i:j])

print(minute_needed(N))
