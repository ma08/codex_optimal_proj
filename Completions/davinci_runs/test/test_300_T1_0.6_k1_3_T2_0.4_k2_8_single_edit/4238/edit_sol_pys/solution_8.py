
# 入力
num = int(input())

# 累積和
s = sum(list(map(int, str(num))))

# 出力
if s % 9 == 0:
    print("Yes")
else:
    print("No")
