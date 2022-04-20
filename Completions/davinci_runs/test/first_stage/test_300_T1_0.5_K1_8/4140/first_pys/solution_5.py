

S = input()

# 1個ずつ見ていく
# 0 -> 1
# 1 -> 0
# という処理を行う
# それぞれの回数を数える
# 小さい方の回数を出力する

# 見ていくときは0のときのみにする
# そうすることで、0のときは1に、1のときは0にすることができる

count0 = 0
count1 = 0

for i in range(len(S)):
    if S[i] == "0":
        count0 += 1
    else:
        count1 += 1

print(min(count0, count1))