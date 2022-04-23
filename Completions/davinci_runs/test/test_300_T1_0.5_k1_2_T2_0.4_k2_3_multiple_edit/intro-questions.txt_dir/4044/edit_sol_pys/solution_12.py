
a, b, x = map(int, input().split())  # 文字列を数値に変換

s = []  # 空のリスト
for _ in range(a):  # リストに0を追加
    s.append('0')
for _ in range(b):
    s.append('1')

for i in range(x):
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
