
a, b, x = map(int, input().split())  # 文字列を数値に変換

s = ['0'] * a + ['1'] * b  # リストに0を追加

for i in range(x):
    if i % 2 == 0:
        s[i], s[i + 1] = s[i + 1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
