

# a = 10, b = 7, x = 100のとき、1の桁のみで計算する
a, b, x = map(int, input().split())
if a + b > x:
    print(0)
    exit()

# 桁数を2以上から計算するため、桁数を決定する
digit = 1
while a * 10**digit + b * (digit + 1) <= x:
    digit += 1

# 桁数を決定したら、最も値が大きい数を計算する
result = (x - b * digit) // a

# 1桁目が9になっている場合、1減らして終了
if result // 10**(digit - 1) == 9:
    result -= 1

print(result)
