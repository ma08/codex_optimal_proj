
S = str(input())
T = str(input())

if S == T:
    print("Yes")
    exit()
for i in range(len(S)):
    S = S[-1] + S[:-1]  # 文字列の先頭の文字を末尾に移動させる
    if S == T:
        print("Yes")
        exit()
print("No")
