

# 文字列を比較して、違う文字がある場合は、文字数をカウントする
# その後、文字数が違う場合は、文字数をカウントし、最後に足す

# 入力
S = input()
T = input()

# 文字列の長さ
S_len = len(S)
T_len = len(T)

# 文字列の比較
count = 0
for i in range(S_len):
    if S[i] != T[i]:
        count += 1

# 文字列の長さが違う場合
if S_len != T_len:
    count += S_len - T_len

# 出力
print(count)