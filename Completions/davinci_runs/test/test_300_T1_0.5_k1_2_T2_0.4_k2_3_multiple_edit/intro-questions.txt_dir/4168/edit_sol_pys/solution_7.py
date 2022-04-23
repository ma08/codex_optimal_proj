
n = int(input()) # 入力

if n == 0: # 0の場合
    print(0)
    exit()

ans = "" # 答え
while n != 0: # -2進数に変換
    if n % (-2) == 0:
        ans += "0"
        n = n // (-2)
    else:
        ans += "1"
        n = n // (-2) + 1

print(ans[::-1])
