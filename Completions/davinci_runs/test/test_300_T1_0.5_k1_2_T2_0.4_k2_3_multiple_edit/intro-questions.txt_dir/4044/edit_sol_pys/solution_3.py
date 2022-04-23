
a, b, x = map(int, input().split())  # a:0の数, b:1の数, x:交換回数

s = []  # 入力を格納するリストを用意
for i in range(a):
    s.append('0')  # 0をa個追加
for i in range(b):
    s.append('1')  # 1をb個追加

for i in range(x):  # 交換回数分ループ
    if i % 2 == 0:  # 偶数回目
        s[i], s[i+1] = s[i+1], s[i]
    else:  # 奇数回目
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
