

S = raw_input()
T = raw_input()

ans = len(S)
for i in range(len(S)-len(T)+1):
    count = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            count += 1
    ans = min(ans, count)

print(ans)

# 文字列の部分文字列を求める問題では，横方向のループを縦方向のループとすることで，効率的に解くことができる．
