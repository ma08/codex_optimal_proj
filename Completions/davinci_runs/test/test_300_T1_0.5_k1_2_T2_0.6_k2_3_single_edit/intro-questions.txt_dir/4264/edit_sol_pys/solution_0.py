

N = int(input())  # 数値をNに代入

count = 0  # カウントを初期化
for i in range(1, N+1):  # 1からNまでの数字を足していく
    count += len(str(i)) % 2  # 奇数なら1、偶数なら0になるので、それを足していく

print(count)
