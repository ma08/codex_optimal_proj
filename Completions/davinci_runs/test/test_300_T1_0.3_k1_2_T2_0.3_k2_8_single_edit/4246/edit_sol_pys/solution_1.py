

# 入力

s = input()
t = input()
# 処理

correct = 0
for i in range(3):
    if s[i] == t[i]:
        correct += 1
# 出力

print(correct)
