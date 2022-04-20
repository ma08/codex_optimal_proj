

n = int(input())  # 入力

if n == 0:  # 0の場合
    print(0)
    exit()

ans = ""
while n != 0:  # 0でない間
    if n % (-2) == 0:
        ans += "0"
        n = n // (-2)  # 商
    else:
        ans += "1"
        n = n // (-2) + 1  # 商+1

print(ans[::-1])  # 出力
