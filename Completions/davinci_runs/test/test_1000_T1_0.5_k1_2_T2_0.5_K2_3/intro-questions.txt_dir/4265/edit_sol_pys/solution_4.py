
s = input()  # 標準入力
t = input()  # 標準入力

ans = 0
for i in range(len(s)):  # len() は文字列の長さを返す関数
    if s[i] != t[i]:  # s[i] は文字列の i 番目の文字
        ans += 1

print(ans)
