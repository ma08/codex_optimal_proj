
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 辞書型に重複しない数字を格納
dic = {}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1

# 辞書型をリストに変換し、値が大きい順に並び替え
dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

# 値の和を取得
sum_dic = 0
for i in range(len(dic)):
    sum_dic += dic[i][1]

# 重複した数字の値がk以下になるまで減らす
while len(dic) > k:
    sum_dic -= dic[len(dic)-1][1]
    dic.pop()

print(n - sum_dic)
