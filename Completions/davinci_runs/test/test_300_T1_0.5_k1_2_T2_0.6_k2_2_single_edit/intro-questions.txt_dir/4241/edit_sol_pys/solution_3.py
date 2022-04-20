

S = input()
T = input()

ans = len(T)
for i in range(len(T)-len(S)+1):
    count = 0
    for j in range(len(S)):
        if T[i+j] != S[j]:
            count += 1
    ans = min(ans, count)

print(ans)

# 文字列の部分文字列を求める問題では，横方向のループを縦方向のループとすることで，効率的に解くことができる．
