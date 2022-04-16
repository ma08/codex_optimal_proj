
S = input()  # 入力

count = 0
for s in S:
    if s == "+":
        count += 1
    else:
        count -= 1
print(count)
