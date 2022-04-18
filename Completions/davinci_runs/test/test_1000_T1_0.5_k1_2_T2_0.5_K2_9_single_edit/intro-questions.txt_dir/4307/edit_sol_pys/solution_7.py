

N = int(input()) # 読み込んだ値をint型に変換

divisors = [1] # 約数を格納するリストを宣言

for i in range(2, int(N**0.5)): # 2から√Nまでの範囲で割り切れるかを確認
    if N % i == 0: # 割り切れた場合
        divisors.append(i) # 割った値を約数のリストに追加
        divisors.append(N // i) # 割った値を約数のリストに追加

if len(divisors) == 8: # 約数が8つあった場合
    print(N) # Nを出力
else:
    print(0) # そうでなければ0を出力
