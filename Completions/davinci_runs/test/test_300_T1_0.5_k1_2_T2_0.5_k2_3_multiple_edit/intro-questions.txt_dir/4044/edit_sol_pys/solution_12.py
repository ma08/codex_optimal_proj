# coding: utf-8

a, b, x = map(int, input().split())  # 入力

s = ['0'] * a + ['1'] * b  # 0と1をつなげる

for i in range(x):
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
