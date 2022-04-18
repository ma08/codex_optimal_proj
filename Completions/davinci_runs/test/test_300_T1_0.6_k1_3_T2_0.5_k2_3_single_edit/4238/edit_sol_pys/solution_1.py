
# 入力
num = int(input())

# 累積和
s = 0
for i in range(len(str(num))):
    s += int(str(num)[i])

# 出力
if s % 9 == 0:
    print("Yes")  # 出力
else:
    print("No")  # 出力
