

s = input()
t = input()

ans = 0
for i in range(len(s)):  # len() は文字列の長さを返す関数
    if s[i] != t[i]:  # s[i] は文字列の i 番目の文字
        ans += 1

print(ans)
