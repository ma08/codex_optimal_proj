

# a = 10, b = 7, x = 1003
a, b, x = map(int, input().split())

# 1の桁のみで計算する
if a + b > x:
    print(0)
    exit()

# 桁数を2以上から計算する
digit = 1
while a * 10**digit + b * (digit + 1) <= x:
    digit += 1

# 桁数を決定したら、最も値が大きい数を計算
result = (x - b * digit) // a

# 1桁目が9になっている場合、1減らして終了
if result // 10**(digit - 1) == 9:
    result -= 1

print(result)
